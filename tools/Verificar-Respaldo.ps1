param(
    [Parameter(Mandatory = $true)]
    [string]$Directorio
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path -LiteralPath $Directorio).Path
$manifest = Get-Content -LiteralPath (Join-Path $root 'manifest.json') -Raw | ConvertFrom-Json
if ($manifest.schema -ne 1 -or $manifest.bytes -ne 4194304 -or @($manifest.files).Count -ne 2) {
    throw 'El manifiesto no corresponde al respaldo completo esperado del QD001.'
}
foreach ($entry in $manifest.files) {
    if ($entry.name -notin @('original-validado-1.bin', 'original-validado-2.bin')) {
        throw 'Nombre de archivo inesperado en el manifiesto.'
    }
    $file = Join-Path $root $entry.name
    if ((Get-Item -LiteralPath $file).Length -ne $manifest.bytes) {
        throw "Tamano incorrecto: $($entry.name)"
    }
    $actual = (Get-FileHash -LiteralPath $file -Algorithm SHA256).Hash
    if ($actual -ne $entry.sha256 -or $actual -ne $manifest.sha256) {
        throw "SHA-256 incorrecto: $($entry.name). No usar para restauracion."
    }
    Write-Output "OK: $($entry.name)"
}
Write-Output 'Integridad de ambas copias comprobada. Esto no demuestra una restauracion funcional.'
