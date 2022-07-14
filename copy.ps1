net use p: \\public\shareddrive

mkdir "C:\Users\$($env:UserName)\AppData\Roaming\Microsoft\Signatures\template_files"
$con = "$($env:UserName)'s_signature.htm"
Copy-Item -Path "\\lpublic\shareddrive\Signature_Creator\$($con)" -Destination "C:\Users\$($env:UserName)\AppData\Roaming\Microsoft\Signatures"
xcopy "\\public\shareddrive\Signature_Creator\template_files" "C:\Users\$($env:UserName)\AppData\Roaming\Microsoft\Signatures\template_files"

# Remove-Item $MyInvocation.MyCommand.Source