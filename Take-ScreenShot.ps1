Add-Type -AssemblyName System.Windows.Forms,System.Drawing

$screens = [Windows.Forms.Screen]::AllScreens
$screen2 = $screens[1]

$top    = ($screen2.Bounds.Top    | Measure-Object -Minimum).Minimum
$left   = ($screen2.Bounds.Left   | Measure-Object -Minimum).Minimum
$width  = ($screen2.Bounds.Right  | Measure-Object -Maximum).Maximum
$height = ($screen2.Bounds.Bottom | Measure-Object -Maximum).Maximum

$bounds   = [Drawing.Rectangle]::FromLTRB($left, $top, $width, $height)
$bmp      = New-Object System.Drawing.Bitmap ([int]$bounds.width), ([int]$bounds.height)
$graphics = [Drawing.Graphics]::FromImage($bmp)

$graphics.CopyFromScreen($bounds.Location, [Drawing.Point]::Empty, $bounds.size)

$bmp.Save("$env:USERPROFILE\Coding\poke-finder\screenshot.png")

$graphics.Dispose()
$bmp.Dispose()