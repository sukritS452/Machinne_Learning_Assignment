$pptxPath = 'c:\Users\Prakriti\Downloads\Sukriti_Sapkota_260180_ML_Assignment\ML_Crop_Dynamics_Presentation_Sukriti_260180.pptx'
$outDir = 'c:\Users\Prakriti\Downloads\Sukriti_Sapkota_260180_ML_Assignment\presentation_slides'
if (-not (Test-Path $outDir)) {
    New-Item -ItemType Directory -Path $outDir | Out-Null
}

$ppt = New-Object -ComObject PowerPoint.Application
try {
    $pres = $ppt.Presentations.Open($pptxPath, 2, 0, 0)
    $pres.SaveAs($outDir, 17)
    $pres.Close()
    Write-Host "Slides successfully exported to PNG!"
} finally {
    $ppt.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
}

Get-ChildItem $outDir
