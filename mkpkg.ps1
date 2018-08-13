Remove-Item packages -Recurse
$outme = pip freeze
pip install --target .\packages\ --no-compile $outme
Set-Location .\packages\
Get-ChildItem -Include *-info -Recurse | Remove-Item -Recurse
7z a packages.zip * -r -sdel
Set-Location ..