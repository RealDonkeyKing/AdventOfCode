#In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). 
#Every other number is adjacent to a symbol and so is a part number; their sum is 4361.
#Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?


with open('list.txt', 'r') as file:
    content = file.readlines()
    for line in content:
        