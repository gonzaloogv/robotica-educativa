"""Extrae o verifica una copia cifrada del QD001 sin acceder al robot."""
import argparse
import hashlib
import json
import os
from pathlib import Path

from cryptography.fernet import Fernet, InvalidToken


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    default_manifest = Path(__file__).resolve().parents[1] / 'backups' / 'acebott-qd001' / 'manifest.json'
    parser.add_argument('--manifest', type=Path, default=default_manifest)
    parser.add_argument('--clave', type=Path, required=True)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument('--verificar', action='store_true', help='Verifica en memoria, sin crear un binario.')
    action.add_argument('--salida', type=Path, help='Archivo nuevo donde extraer el .bin. No sobrescribe.')
    args = parser.parse_args()
    try:
        manifest_path = args.manifest.resolve(strict=True)
        manifest = json.loads(manifest_path.read_text(encoding='utf-8-sig'))
        if manifest.get('schema') != 1 or manifest.get('encryption') != 'Fernet':
            raise ValueError('Formato de manifiesto no soportado.')
        if manifest.get('encrypted_file') != 'firmware-original.fernet':
            raise ValueError('Nombre de archivo cifrado inesperado.')
        encrypted = (manifest_path.parent / manifest['encrypted_file']).read_bytes()
        if len(encrypted) != manifest['encrypted_bytes']:
            raise ValueError('Tamano incorrecto del archivo cifrado.')
        if hashlib.sha256(encrypted).hexdigest() != manifest['encrypted_sha256']:
            raise ValueError('SHA-256 incorrecto del archivo cifrado.')
        data = Fernet(args.clave.read_bytes().strip()).decrypt(encrypted)
        if len(data) != 4194304 or len(data) != manifest['original_bytes']:
            raise ValueError('La imagen recuperada no tiene los 4 MB esperados.')
        digest = hashlib.sha256(data).hexdigest()
        if digest != manifest['original_sha256']:
            raise ValueError('SHA-256 incorrecto de la imagen recuperada.')
        if args.salida is not None:
            if args.salida.suffix.lower() != '.bin':
                raise ValueError('La salida debe tener extension .bin.')
            with args.salida.open('xb') as output:
                output.write(data)
                output.flush()
                os.fsync(output.fileno())
            print(f'Imagen extraida: {args.salida}')
        print(f'OK: {len(data)} bytes, SHA-256 {digest}')
        print('No se accedio al robot. La restauracion en la placa sigue sin ensayarse.')
    except InvalidToken:
        parser.exit(1, 'Error: la clave no corresponde o la copia cifrada fue alterada.\n')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, f'Error: {exc}\n')


if __name__ == '__main__':
    main()
