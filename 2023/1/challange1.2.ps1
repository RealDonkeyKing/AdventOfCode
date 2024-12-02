$numberword = @("one","two","three","four","five","six","seven","eigh","nine")
$numberarr = @(1,2,3,4,5,6,7,8,9)
$list = Get-Content .\list.txt
$sum = 0

foreach ($line in $list)
{

    for($i=0;$i -lt 9; $i++)
    {
        $line = $line.Replace($numberword[$i], $numberword[$i]+$numberarr[$i])
        #$line+"line"     
    }
    $line >> log.log
    $line = $line -replace "[^0-9]" , ''
     $line >> log.log
    #$line = $line -split "[^\d]" -join ''
    [int]$number = $($line[0]+$line[-1]) 
    $number >> log.log
    $sum=$sum+$number   
}

   Write-Host $sum 

#53196 meins
#53242 [int]$number = $($line[0]+$line[-1])
#53312 lösung


