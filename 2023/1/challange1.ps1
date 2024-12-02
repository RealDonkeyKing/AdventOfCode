$list = Get-Content .\list.txt
$sum = 0
foreach ($line in $list)
{
    $line = $line -replace "[^0-9]" , ''
    $number = $line[0]+""+$line[-1]
    $sum+=$number
    
}
Write-Host $sum