sum_id = 0
with open('list.txt', 'r') as file:
    content = file.readlines()
    for line in content:
        # Extract game ID
        id = line.split(" ")[1].split(":")[0]

        # Split rounds
        rounds = line.split(":")[1].strip().split(";")

        valid_game = True
        for round_str in rounds:
            balls = {"red": 0, "blue": 0, "green": 0}
            for color_count in round_str.strip().split(","):
                color_count = color_count.strip()
                if "red" in color_count:
                    balls["red"] = int(color_count.split()[0])
                elif "blue" in color_count:
                    balls["blue"] = int(color_count.split()[0])
                elif "green" in color_count:
                    balls["green"] = int(color_count.split()[0])
            if balls["red"] > 12 or balls["green"] > 13 or balls["blue"] > 14:
                valid_game = False
                break

        if valid_game:
            sum_id += int(id)
    print(sum_id)
            
sum_total = 0
with open('list.txt', 'r') as file:
    content = file.readlines()
    for line in content:
        # Initialize max values
        max_balls = {"red": 0, "green": 0, "blue": 0}

        # Split rounds
        rounds = line.split(":")[1].strip().split(";")

        for round_str in rounds:
            # Temporary storage for this round
            round_balls = {"red": 0, "green": 0, "blue": 0}
            for color_count in round_str.strip().split(","):
                color_count = color_count.strip()
                if "red" in color_count:
                    round_balls["red"] = int(color_count.split()[0])
                elif "blue" in color_count:
                    round_balls["blue"] = int(color_count.split()[0])
                elif "green" in color_count:
                    round_balls["green"] = int(color_count.split()[0])

            # Update max values
            for color in max_balls:
                max_balls[color] = max(max_balls[color], round_balls[color])

        # Multiply the max values and add to total
        product = max_balls["red"] * max_balls["green"] * max_balls["blue"]
        sum_total += product

    print(sum_total)
            