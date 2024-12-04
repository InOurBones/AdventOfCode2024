with open("./04/input.txt", "r") as file:
    input = file.read().split("\n")

total = 0
for y in range(1, len(input) - 1):
    for x in range(1, len(input[0]) - 1):
        if input[y][x] != "A":
            continue

        bot_left = input[y-1][x-1]
        bot_right = input[y-1][x+1]
        top_left = input[y+1][x-1]
        top_right = input[y+1][x+1]
        
        big_stronk = bot_left + bot_right + top_left + top_right
        if big_stronk.count("M") != 2 or big_stronk.count("S") != 2:
            continue
        
        if bot_left != top_right:
            total += 1
print(total)
        