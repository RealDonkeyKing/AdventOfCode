# Given strings
$string1 = "The price of the item is fivetwo dollars."
$string2 = "I have seven apples and three oranges."
$string3 = "zmeightwohkgs6"

# Dictionary for mapping namewords to numbers
$namewordsMapping = @{
    'one'   = '1'
    'two'   = '2'
    'three' = '3'
    'four'  = '4'
    'five'  = '5'
    'six'   = '6'
    'seven' = '7'
    'eight' = '8'
    'nine'  = '9'
}

# Function to replace namewords with numbers
function Replace-NamewordsWithNumbers ($inputString) {
    $resultString = $inputString -replace "(?i)(?<=^|\W)(" + (($namewordsMapping.Keys | ForEach-Object {[regex]::Escape($_)}) -join '|') + ")(?=\W|$)", {
        param($match)
        return $namewordsMapping[$match.Value.ToLower()]
    }
    return $resultString
}

# Replace namewords with numbers in each string
$resultString1 = Replace-NamewordsWithNumbers $string1
$resultString2 = Replace-NamewordsWithNumbers $string2
$resultString3 = Replace-NamewordsWithNumbers $string3

# Print the results
Write-Host "Original String 1: $string1"
Write-Host "Updated String 1: $resultString1`n"
Write-Host "Original String 2: $string2"
Write-Host "Updated String 2: $resultString2`n"
Write-Host "Original String 3: $string3"
Write-Host "Updated String 3: $resultString3"
