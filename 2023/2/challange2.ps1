#
#The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
#In the example above, games 1, 2, and 5 would have been possible
#
#Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
$teststring = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green";
$gameids = $teststring.split('Game ')[1].split(':')[0];
$teststring=$teststring.replace(",","");
$teststring=$teststring.replace(";","").split(':')[1].split(" ");
#$i=$teststring.length;
$numarr = @();
$colors = @();
$2ndhalf = @();
$red = 0;
$blue = 0;
$green = 0;
for($i=1;$i -lt $teststring.length;$i=$i+2)
{
   
        #color
        #write-host $i + $string;
        $colors += $teststring[$i]+" "+$teststring[$i+1];
        write-host $colors[$i]"colors";
       $2ndhalf= $colors[$i].split(" ");
       #write-host "2ndhalf"$2ndhalf;
        switch($2ndhalf[1])
        {
            "*red"{$red+=$colors[$i].split(" ")[1]}
            "*blue"{$blue+=$colors[$i].split(" ")[1]}
            "*green"{$green+=$colors[$i].split(" ")[1]}
        }
}    
write-host $colors[-1];
write-host "Red:" $red;
write-host "Green:" $green;
write-host "Bue:" $blue;
