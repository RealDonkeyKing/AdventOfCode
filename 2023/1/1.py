import re

# Map of word numbers to digits
word_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

# Build regex that captures digits and spelled-out numbers
pattern = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")

total = 0

with open('input.txt') as file:
    for line in file:
        line = line.strip()
        matches = [m.group(1) for m in pattern.finditer(line)]
        
        # Convert word matches to digits
        digits = [word_to_digit.get(m, m) for m in matches]
        
        if digits:
            number = int(digits[0] + digits[-1])
            total += number

print(total)
