#The levels are either all increasing or all decreasing.
#Any two adjacent levels differ by at least one and at most three.
#How many reports are safe?
# Solution1 = 390
# Solution2 = 439
def iscorrect(row):
    # Array/ list that contains a check of the next element subtract by the current element 
    # will later check if the value is between 1 and 3
    # while the array is not yet 1 before end

    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    #sets used to store mulitple valuses in a var
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True
    return False

# get rows into array
data = [[int(y) for y in x.split(' ')] for x in open('input.txt').read().split('\n')]

safe_count = sum([iscorrect(row) for row in data])
print(safe_count)
#Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

#row[:i] is at slicing, if i is 2 then the first two get sliced
safe_count = sum([any([iscorrect(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in data])
print(safe_count)
            