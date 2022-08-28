mkdir -Path "C:\Users\$([environment]::Username)\AppData\Roaming\Microsoft\Signatures\template_files"
$con = "$([environment]::Username)'s_signature.htm"
Copy-Item -Path "\\shareddriver\$($con)" -Destination "C:\Users\$([environment]::Username)\AppData\Roaming\Microsoft\Signatures"
xcopy "\\sharedrive\template_files" "C:\Users\$([environment]::Username)\AppData\Roaming\Microsoft\Signatures\template_files"

$path1 =  "C:\Users\$([environment]::Username)\AppData\Roaming\Microsoft\Signatures\template_files"
$path2 = "C:\Users\$([environment]::Username)\AppData\Roaming\Microsoft\Signatures\$($con)"

$Test_Path = Test-Path -Path $path1 
$Test_Path_2 = Test-Path -Path $path2 -PathType Leaf
$command = Remove-Item -Path "\\shareddrive\$($con)"

if ($Test_Path_2 -and $Test_Path -eq $false)
    {
        Write-Host "Operation Failed: Unable to Copy files."
    }

elseif ($Test_Path_2 -and $Test_Path -eq $true)
    { 
    $command
    $prompt = Write-Host "Added" + " " + "$([envrionment]::Username)'s Signature. Press 'Q' to quit."
    $prompt 
