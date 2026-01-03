
list=["24-46","124420-259708","584447-720297","51051-105889","6868562486-6868811237","55-116","895924-1049139","307156-347325","372342678-372437056","1791-5048","3172595555-3172666604","866800081-866923262","5446793-5524858","6077-10442","419-818","57540345-57638189","2143479-2274980","683602048-683810921","966-1697","56537997-56591017","1084127-1135835","1-14","2318887654-2318959425","1919154462-1919225485","351261-558210","769193-807148","4355566991-4355749498","809094-894510","11116-39985","9898980197-9898998927","99828221-99856128","9706624-9874989","119-335"]
list = ["11-22","95-115","998-1012","1188511880-1188511890","222220-222224","1698522-1698528","446443-446449","38593856-38593862","565653-565659","824824821-824824827","2121212118-2121212124"]

sum_invalid_ids = 0
#print(list[0])

for area in list:
    split_area = area.split("-")
    first_half = split_area[0]
    second_half = split_area[1]
    #check if number is even

    combined_first_first = str(first_half)+str(first_half)
    combined_second_second = str(second_half)+str(second_half)

    if int(first_half) % 2:
        print(first_half)
        first_part, second_part =  first_half[:len(first_half)//2], first_half[len(first_half)//2:]
        print(first_part+" "+second_part)
        if( first_part == second_part):
            sum_invalid_ids+=int(first_half)
    if int(second_half) % 2:
        print(second_half)
        first_part, second_part =  second_half[:len(second_half)//2], second_half[len(second_half)//2:]
        print(first_part+" "+second_part)
        if( first_part == second_part):
            sum_invalid_ids+=int(second_half)
    print(combined_first_first)
    if int(combined_first_first) > int(first_half) & int(combined_first_first) < int(second_half):
        sum_invalid_ids+=int(combined_first_first)
    
print("Sum invalid ids:"+str(sum_invalid_ids))


#check if first half == second half of a string


#if not check if firsthalf === second half within range




