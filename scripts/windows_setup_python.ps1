$url = "https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe"
$dest = ".\python-3.12.1-amd64.exe"
Invoke-WebRequest -Uri $url -OutFile $dest

Start-Process -FilePath $dest -ArgumentList "/quiet InstallAllUsers=0 PrependPath=1" -Wait

$t = "$env:LOCALAPPDATA\Programs\Python\Python312\python"
& $t -m pip install --upgrade pip --no-warn-script-location
& $t -m pip install --user pipx --no-warn-script-location

$t = "$env:APPDATA\Python\Python312\Scripts\pipx"
& $t install poetry

Function Set-PathVariable {
    param (
        [string]$AddPath,
        [string]$RemovePath,
        [ValidateSet('Process', 'User', 'Machine')]
        [string]$Scope = 'Process'
    )
    $regexPaths = @()
    if ($PSBoundParameters.Keys -contains 'AddPath') {
        $regexPaths += [regex]::Escape($AddPath)
    }

    if ($PSBoundParameters.Keys -contains 'RemovePath') {
        $regexPaths += [regex]::Escape($RemovePath)
    }

    $arrPath = [System.Environment]::GetEnvironmentVariable('PATH', $Scope) -split ';'
    foreach ($path in $regexPaths) {
        $arrPath = $arrPath | Where-Object { $_ -notMatch "^$path\\?" }
    }
    $value = ($arrPath + $addPath) -join ';'
    [System.Environment]::SetEnvironmentVariable('PATH', $value, $Scope)
}
Set-PathVariable -AddPath %USERPROFILE%\.local\bin -Scope User
