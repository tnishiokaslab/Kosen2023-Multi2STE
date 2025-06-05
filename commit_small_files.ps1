# ファイル1つあたりの最大サイズ
$maxSingleSize = 20MB

# コミットするファイルの合計サイズの上限
$maxTotalSize = 30MB

# git status -s で変更・追加されたファイルリストを取得
$files = git status -s | ForEach-Object {
    $parts = $_ -split '\s+'
    if ($parts.Length -ge 2) { $parts[1] }
}

$selectedFiles = @()
$totalSize = 0

foreach ($file in $files) {
    if (Test-Path $file) {
        $size = (Get-Item $file).Length
        if ($size -le $maxSingleSize) {
            if (($totalSize + $size) -le $maxTotalSize) {
                $selectedFiles += $file
                $totalSize += $size
            } else {
                break  # 合計サイズオーバーしたら終了
            }
        }
    }
}

if ($selectedFiles.Count -gt 0) {
    Write-Host "Adding files (合計 $([math]::Round($totalSize / 1MB, 2)) MB):"
    $selectedFiles | ForEach-Object { Write-Host " - $_" }
    git add $selectedFiles
    git commit -m "Auto commit: files smaller than $($maxSingleSize / 1MB)MB, total under $($maxTotalSize / 1MB)MB"
    git push origin main
} else {
    Write-Host "No files under the size limit to commit."
}
