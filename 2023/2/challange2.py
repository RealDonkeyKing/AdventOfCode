sum_id = 0
with open('list.txt', 'r') as file:
    content = file.readlines()
    for line in content:
        balls = {
        "red":0,
        "blue":0,
        "green":0,
        }
        #Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        #print(line)
        id= line.split(" ")
        id = id[1].split(":")
        #print(id[0])
        #Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        #print(line.split(":")[1].replace(";",",").split(";")[0])
        line = line.split(":")[1].replace(",",";").split(";")
        #print(line[1])  
        
        
        for color in line:
            if color.count("red") == 1:
                balls["red"]+=int(color.split( )[0])
            if color.count("blue") == 1:
                balls["blue"]+=int(color.split( )[0])
            if color.count("green") == 1:
                balls["green"]+=int(color.split( )[0])
                
                
        if balls["red"] > 12 or balls["green"] > 13 or balls["blue"] > 14:
           print(balls["red"], balls["green"], balls["blue"])
        else:
            print(line)
            print(balls["red"], balls["green"], balls["blue"])
            print(id[0])
            sum_id+=int(id[0])
    print(sum_id)
            
            