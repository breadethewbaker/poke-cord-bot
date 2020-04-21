Set-Location $PSScriptRoot
Set-Content ./clipboard.txt -NoNewLine -Value ''

./Take-ScreenShot
./template_scan.py
./rev_img_search2.py

$clipboard = Get-Content .\clipboard.txt -Raw
Set-Clipboard -Value $clipboard
Write-Output 'Done'