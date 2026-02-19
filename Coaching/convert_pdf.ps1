$chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$baseDir = "d:\Workspace\AI_academy\AI_academy\Coaching"
$outputDir = Join-Path $baseDir "pdf"

if (!(Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir
}

# 01_데이터_개념_
$prefix = "01_$([char]0xB370)$([char]0xC774)$([char]0xD130)_$([char]0xAC1C)$([char]0xB150)_"

# Use wildcard to get files and avoid encoding issues in script writing
$files = Get-ChildItem -Path $baseDir -Filter "01_*.html" -File

Write-Host "Total .html files found starting with 01_: $($files.Count)"

foreach ($file in $files) {
    if ($file.Name -match "_(\d+)\.html$") {
        $num = $matches[1]
        $n = [int]$num
        if ($n -ge 1 -and $n -le 23) {
            $tempOutput = Join-Path $outputDir "temp_$num.pdf"
            $finalName = $prefix + $num + ".pdf"
            $finalOutput = Join-Path $outputDir $finalName
            
            Write-Host "Converting $($file.Name) to $finalName ..."
            
            # Use file URL from the actual object to be safe
            $fileUrl = "file:///" + $file.FullName.Replace("\", "/")
            
            # Print to PDF. Headless mode required.
            # Screen size 1280x720 at 96 DPI corresponds to 13.33 x 7.5 inches.
            $process = Start-Process $chromePath -ArgumentList "--headless", "--print-to-pdf=`"$tempOutput`"", "--no-margins", "--paper-width=13.33", "--paper-height=7.5", "`"$fileUrl`"" -Wait -PassThru
            
            if (Test-Path $tempOutput) {
                # Move to final name with exact Korean characters
                Move-Item -LiteralPath $tempOutput -Destination $finalOutput -Force
            }
            else {
                Write-Warning "Failed to convert $($file.Name)"
            }
        }
    }
}
Write-Host "PDF Conversion completed."
