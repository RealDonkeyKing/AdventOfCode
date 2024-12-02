#50 stars
#kleinste links mit kleinste rechts

#herausfinden wie weit entfernt, das zusammen addieren
# Open the text file
#Part 1
sum = 0
arr1 = []
arr2 = []
with open('input.txt', 'r') as file:
    # Read each line from the file
    for line in file:
        # Strip any leading/trailing whitespace and split by spaces
        values = line.strip().split('   ')
        arr1.append(values[0])
        arr2.append(values[1])
    arr1.sort()
    arr2.sort()  
    for i in range(0, len(arr1)):
        tempsum = int(arr1[i]) - int(arr2[i])
        if tempsum < 0 :
            tempsum = tempsum*-1
        #print(tempsum)
        sum+=tempsum
        # Print or process the values
    #print(sum)
#Part 2
#how often does the number from left appears in right
sum = 0
arr1 = []
arr2 = []
with open('input.txt', 'r') as file:
    # Read each line from the file
    for line in file:
        # Strip any leading/trailing whitespace and split by spaces
        values = line.strip().split('   ')
        arr1.append(values[0])
        arr2.append(values[1])
    arr1.sort()
    arr2.sort()  
    for i in range(0, len(arr1)):
        tempsum=arr2.count(arr1[i])
        sum+=int(tempsum)*int(arr1[i])
        print(sum)
print(sum)