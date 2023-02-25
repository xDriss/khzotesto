$ie = New-Object -ComObject "InternetExplorer.Application"
$ie.Navigate("https://yip.su/Winners")
$ie.Visible = $true
