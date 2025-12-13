import re
found = 0
def searchhorizontal(lines):
    found = []
    for line in lines:
        found += re.findall(r"XMAS|XAMX", line)
        #print(line)
    amountfound = len(found)
    return amountfound
def searchvertical(lines):
    found = 0
    
    #lines[0] = 1.Zeile
    #lines[0][4] = 5. Buchstabe 1. Zeile
    for j in range(len(lines)-3): #Zeilen
        #print(j)
        for i in range(len(lines[j])):#Buchstaben in den Zeilen
            if lines[j][i] == "X" and lines[j+1][i] == "M" and lines[j+2][i] == "A" and lines[j+3][i] == "S":
                found+=1
            if lines[j][i] == "S" and lines[j+1][i] == "A" and lines[j+2][i] == "M" and lines[j+3][i] == "X":
                found+=1
    return found

def searchdiagonal(lines):
    found = 0
    #lines[0] = 1.Zeile
    #lines[0][4] = 5. Buchstabe 1. Zeile
    for z in range(2):
        if z:
            lines=list(reversed(lines))
        for j in range(len(lines)-3): #Zeilen
            #print(j)
            for i in range(len(lines[j])-2):#Buchstaben in den Zeilen
                if lines[j][i] == "X" and lines[j+1][i+1] == "M" and lines[j+2][i+2] == "A" and lines[j+3][i+3] == "S":
                    found+=1
                if lines[j][i] == "S" and lines[j+1][i+1] == "A" and lines[j+2][i+2] == "M" and lines[j+3][i+3] == "X":
                    found+=1
    return found
with open('input2.txt') as file:
    lines = file.read().strip().split("\n")
found+=searchhorizontal(lines)
found+=searchvertical(lines)
found+=searchdiagonal(lines)
print("XMAS as word:"+str(found))


#####
def count_xmas_occurrences(grid):
    word = "XMAS"
    word_len = len(word)
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Direction vectors for 8 directions (horizontal, vertical, diagonal)
    directions = [
        (0, 1),   # Horizontal (right)
        (0, -1),  # Horizontal (left)
        (1, 0),   # Vertical (down)
        (-1, 0),  # Vertical (up)
        (1, 1),   # Diagonal (down-right)
        (1, -1),  # Diagonal (down-left)
        (-1, 1),  # Diagonal (up-right)
        (-1, -1)  # Diagonal (up-left)
    ]

    def is_valid(x, y):
        """Check if (x, y) is within bounds."""
        return 0 <= x < rows and 0 <= y < cols

    def check_direction(x, y, dx, dy):
        """Check if the word exists starting from (x, y) in direction (dx, dy)."""
        for k in range(word_len):
            nx, ny = x + k * dx, y + k * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[k]:
                return False
        return True

    # Iterate through the grid and search in all directions
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if check_direction(x, y, dx, dy):
                    count += 1

    return count

# Input einlesen
with open("input2.txt", "r") as f:
    lines = [line.strip() for line in f]

# Ergebnis berechnen
result = count_xmas_occurrences(lines)
print("Total occurrences of XMAS:", result)

def count_xmas_pattern(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Funktion, um zu prüfen, ob das Muster an Position (x, y) existiert
    def is_xmas_pattern(x, y):
        # Überprüfen, ob das Muster innerhalb der Grenzen liegt
        if x - 1 < 0 or x + 1 >= rows or y - 1 < 0 or y + 1 >= cols:
            return False
        
        # Prüfe das Muster
        return (
            grid[x - 1][y - 1] == "M" and grid[x - 1][y + 1] == "S" and
            grid[x][y] == "A" and
            grid[x + 1][y - 1] == "M" and grid[x + 1][y + 1] == "S"
        )
    def is_xmas_pattern2(x, y):
        # Überprüfen, ob das Muster innerhalb der Grenzen liegt
        if x - 1 < 0 or x + 1 >= rows or y - 1 < 0 or y + 1 >= cols:
            return False
        
        # Prüfe das Muster
        return (
            grid[x - 1][y - 1] == "S" and grid[x - 1][y + 1] == "M" and
            grid[x][y] == "A" and
            grid[x + 1][y - 1] == "S" and grid[x + 1][y + 1] == "M"
        )

    # Iteriere durch das Raster
    for x in range(rows):
        for y in range(cols):
            if is_xmas_pattern(x, y):
                count += 1
            if is_xmas_pattern2(x, y):
                count += 1

    return count

# Input einlesen
with open("input2.txt", "r") as f:
    lines = [line.strip() for line in f]

# Ergebnis berechnen
result = count_xmas_pattern(lines)
print("Total X-MAS patterns:", result)



#Result:2575 


#Task 2: Dummy Result 9 X-MAS

