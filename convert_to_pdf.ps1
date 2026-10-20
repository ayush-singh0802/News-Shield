param (
    [string]$InputPath,
    [string]$OutputPath
)

$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $doc = $word.Documents.Open($InputPath, $false, $true)
    $wdFormatPDF = 17
    $doc.SaveAs([ref]$OutputPath, [ref]$wdFormatPDF)
    $doc.Close([ref]$false)
    Write-Output "Successfully converted $InputPath to $OutputPath"
} catch {
    Write-Error $_
} finally {
    $word.Quit([ref]$false)
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
}
