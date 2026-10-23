'use strict';

// Adaptación local de un proyecto de ACECode. No abre puertos ni ejecuta bloques.
const fs = require('fs');
const path = require('path');
const zlib = require('zlib');
const crypto = require('crypto');
const assert = require('assert/strict');

const table = Array.from({length: 256}, (_, n) => {
  for (let i = 0; i < 8; i++) n = (n & 1) ? 0xedb88320 ^ (n >>> 1) : n >>> 1;
  return n >>> 0;
});
function crc32(data) {
  let crc = 0xffffffff;
  for (const byte of data) crc = table[(crc ^ byte) & 255] ^ (crc >>> 8);
  return (crc ^ 0xffffffff) >>> 0;
}
function readZip(buffer) {
  let end = buffer.length - 22;
  while (end >= Math.max(0, buffer.length - 65557) && buffer.readUInt32LE(end) !== 0x06054b50) end--;
  assert(end >= 0 && buffer.readUInt32LE(end) === 0x06054b50, 'ZIP sin directorio final');
  assert.equal(buffer.readUInt16LE(end + 4), 0, 'ZIP multidisco no soportado');
  const count = buffer.readUInt16LE(end + 10);
  let offset = buffer.readUInt32LE(end + 16);
  const entries = [];
  for (let i = 0; i < count; i++) {
    assert.equal(buffer.readUInt32LE(offset), 0x02014b50);
    const nameLength = buffer.readUInt16LE(offset + 28);
    const extraLength = buffer.readUInt16LE(offset + 30);
    const commentLength = buffer.readUInt16LE(offset + 32);
    const method = buffer.readUInt16LE(offset + 10);
    assert([0, 8].includes(method), 'Compresión ZIP no soportada');
    assert.equal(buffer.readUInt16LE(offset + 8) & 1, 0, 'ZIP cifrado no soportado');
    const local = buffer.readUInt32LE(offset + 42);
    assert.equal(buffer.readUInt32LE(local), 0x04034b50);
    const begin = local + 30 + buffer.readUInt16LE(local + 26) + buffer.readUInt16LE(local + 28);
    const compressedSize = buffer.readUInt32LE(offset + 20);
    const compressed = buffer.subarray(begin, begin + compressedSize);
    const raw = method === 8 ? zlib.inflateRawSync(compressed) : compressed;
    const expectedCRC = buffer.readUInt32LE(offset + 16);
    assert.equal(raw.length, buffer.readUInt32LE(offset + 24));
    assert.equal(crc32(raw), expectedCRC, 'CRC incorrecto');
    entries.push({
      name: buffer.subarray(offset + 46, offset + 46 + nameLength).toString('utf8'),
      method, raw, compressed, crc: expectedCRC,
      time: buffer.readUInt16LE(offset + 12), date: buffer.readUInt16LE(offset + 14)
    });
    offset += 46 + nameLength + extraLength + commentLength;
  }
  return entries;
}
function writeZip(entries) {
  const locals = [], central = [];
  let position = 0;
  for (const entry of entries) {
    const name = Buffer.from(entry.name, 'utf8');
    const h = Buffer.alloc(30);
    h.writeUInt32LE(0x04034b50); h.writeUInt16LE(20, 4); h.writeUInt16LE(0x800, 6);
    h.writeUInt16LE(entry.method, 8); h.writeUInt16LE(entry.time, 10); h.writeUInt16LE(entry.date, 12);
    h.writeUInt32LE(entry.crc, 14); h.writeUInt32LE(entry.compressed.length, 18);
    h.writeUInt32LE(entry.raw.length, 22); h.writeUInt16LE(name.length, 26);
    const c = Buffer.alloc(46);
    c.writeUInt32LE(0x02014b50); c.writeUInt16LE(20, 4); c.writeUInt16LE(20, 6);
    c.writeUInt16LE(0x800, 8); c.writeUInt16LE(entry.method, 10);
    c.writeUInt16LE(entry.time, 12); c.writeUInt16LE(entry.date, 14); c.writeUInt32LE(entry.crc, 16);
    c.writeUInt32LE(entry.compressed.length, 20); c.writeUInt32LE(entry.raw.length, 24);
    c.writeUInt16LE(name.length, 28); c.writeUInt32LE(position, 42);
    locals.push(h, name, entry.compressed); central.push(c, name);
    position += h.length + name.length + entry.compressed.length;
  }
  const directory = Buffer.concat(central), end = Buffer.alloc(22);
  end.writeUInt32LE(0x06054b50); end.writeUInt16LE(entries.length, 8); end.writeUInt16LE(entries.length, 10);
  end.writeUInt32LE(directory.length, 12); end.writeUInt32LE(position, 16);
  return Buffer.concat([...locals, directory, end]);
}
const [input, output] = process.argv.slice(2);
if (!input || !output) {
  console.error('Uso: node tools/preparar_sta.js ORIGINAL.sb3 DESTINO.sb3');
  process.exit(1);
}
assert(!fs.existsSync(output), 'No se sobrescribe un proyecto existente');
const original = fs.readFileSync(input), entries = readZip(original);
const projectEntry = entries.find(e => e.name === 'project.json');
assert(projectEntry, 'Falta project.json');
const project = JSON.parse(projectEntry.raw.toString('utf8'));
assert.equal(project.mainboard, 'ESP32');
assert.equal(project.scratchMode, 'upload');
const previous = structuredClone(project);
const matches = project.targets.flatMap((t, targetIndex) => Object.entries(t.blocks || {})
  .filter(([, b]) => b && b.opcode === 'WIFI_AP').map(([id]) => ({targetIndex, id})));
assert.equal(matches.length, 1, 'Se esperaba un solo inicio AP en el programa completo');
const {targetIndex, id} = matches[0], target = project.targets[targetIndex], blocks = target.blocks;
const ap = blocks[id], parentId = ap.parent, nextId = ap.next;
assert.equal(blocks[parentId].next, id); assert(nextId && blocks[nextId]);
const names = ['sta_close_ap', 'sta_log_connect', 'sta_wait_connected', 'sta_status', 'sta_log_ip_label', 'sta_log_ip', 'sta_ip'];
for (const key of names) assert(!blocks[key], 'ID STA ya existente');
function block(opcode, parent, next, inputs = {}, fields = {}) {
  return {opcode, next, parent, inputs, fields, shadow: false, topLevel: false};
}
blocks[parentId].next = 'sta_close_ap';
blocks.sta_close_ap = block('CLOSE_AP', parentId, 'sta_log_connect');
blocks.sta_log_connect = block('log', 'sta_close_ap', id,
  {STRING: [1, [10, 'Conectando a Wi-Fi en modo STA...']]}, {BAUD_RATE: ['115200', null]});
ap.opcode = 'CONNECT_WIFI'; ap.fields = {}; ap.parent = 'sta_log_connect'; ap.next = 'sta_wait_connected';
ap.inputs.NAME = [1, [10, 'CONFIGURAR_WIFI_2_4_GHZ']];
ap.inputs.PASSWORD = [1, [10, 'CONFIGURAR_CLAVE_WIFI']];
blocks.sta_wait_connected = block('control_wait_until', id, 'sta_log_ip_label', {CONDITION: [2, 'sta_status']});
blocks.sta_status = block('WIFI_INFO', 'sta_wait_connected', null, {}, {INFO: ['STATUS', null]});
blocks.sta_log_ip_label = block('log', 'sta_wait_connected', 'sta_log_ip',
  {STRING: [1, [10, 'IP del robot en la red local:']]}, {BAUD_RATE: ['115200', null]});
blocks.sta_log_ip = block('log', 'sta_log_ip_label', nextId,
  {STRING: [3, 'sta_ip', [10, '0.0.0.0']]}, {BAUD_RATE: ['115200', null]});
blocks.sta_ip = block('WIFI_INFO', 'sta_log_ip', null, {}, {INFO: ['IP', null]});
blocks[nextId].parent = 'sta_log_ip';
// Todos los bloques originales ajenos al encadenamiento de red quedan idénticos.
const changed = new Set([id, parentId, nextId]);
previous.targets.forEach((t, ti) => {
  for (const [bid, b] of Object.entries(t.blocks || {})) {
    if (ti !== targetIndex || !changed.has(bid)) assert.deepEqual(project.targets[ti].blocks[bid], b);
  }
});
assert.deepEqual(project.extensions, previous.extensions);
projectEntry.raw = Buffer.from(JSON.stringify(project), 'utf8');
projectEntry.method = 8; projectEntry.compressed = zlib.deflateRawSync(projectEntry.raw); projectEntry.crc = crc32(projectEntry.raw);
const zipped = writeZip(entries), verified = readZip(zipped);
assert.deepEqual(JSON.parse(verified.find(e => e.name === 'project.json').raw.toString('utf8')), project);
for (const e of entries.filter(e => e.name !== 'project.json')) assert.deepEqual(verified.find(v => v.name === e.name).raw, e.raw);
fs.mkdirSync(path.dirname(output), {recursive: true}); fs.writeFileSync(output, zipped, {flag: 'wx'});
const modes = Object.values(blocks).filter(b => b.opcode === 'carMotorV2_carMode').map(b => b.fields.ONE[0]);
const manifest = {
  source_file: path.basename(input), source_sha256: crypto.createHash('sha256').update(original).digest('hex'),
  output_file: path.basename(output), output_sha256: crypto.createHash('sha256').update(zipped).digest('hex'),
  source_blocks: Object.keys(previous.targets[targetIndex].blocks).length, output_blocks: Object.keys(blocks).length,
  network: 'STA; AP cerrado; espera conexion y muestra IP a 115200',
  credentials: 'Solo marcadores, sin datos reales', preserved_modes: modes,
  unrelated_original_blocks_unchanged: true, assets_unchanged: true,
  hardware_uploaded: false, hardware_tested: false,
  note: 'Los GPIO y la logica del fabricante se conservan. Preparacion de archivo, no prueba del robot.'
};
fs.writeFileSync(path.join(path.dirname(output), 'manifest-sta.json'), JSON.stringify(manifest, null, 2) + '\n');
console.log(JSON.stringify(manifest, null, 2));
