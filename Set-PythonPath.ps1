param(
    [Parameter(Mandatory=$true)] [String] $PythonDistDir
)

$fixedPythonDistDir = Resolve-Path $PythonDistDir.Trim('\')
$fixedPythonScriptsDir = Resolve-Path (Join-Path $env:APPDATA Python\Scripts).Trim('\')
$currentPythonDir = Split-Path -Path (Get-Command python.exe).Path

$searchPaths = $env:PATH.Split(';') | Where { -not $_.StartsWith($currentPythonDir) }
$newSearchPaths = @($fixedPythonDistDir, $fixedPythonScriptsDir) + $searchPaths
$env:PATH = $newSearchPaths -join ";"
