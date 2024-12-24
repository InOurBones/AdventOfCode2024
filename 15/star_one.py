with open("./15/input.txt", "r") as file:
    grid, steps = file.read().split("\n\n")
grid = [list(x) for x in grid.split("\n")]
steps = list(steps.replace("\n", ""))

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "@":
            robot = (x, y)
            break

moves = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0)
}

def add_num(a, b):
    return a + b

while steps:
    dir = moves[steps.pop(0)]
    new_x, new_y = tuple(map(add_num, robot, dir))
    if grid[new_y][new_x] == "#":
        continue
    if grid[new_y][new_x] == ".":
        grid[new_y][new_x] = "@"
        grid[robot[1]][robot[0]] = "."
        robot = (new_x, new_y)
        continue
    
    # grid[new_y][new_x] == "O"
    while grid[new_y][new_x] == "O":
        new_x, new_y = tuple(map(add_num, (new_x, new_y), dir))
    if grid[new_y][new_x] == "#":
        continue
    grid[new_y][new_x] = "O"
    grid[robot[1] + dir[1]][robot[0] + dir[0]] = "@"
    grid[robot[1]][robot[0]] = "."
    robot = (robot[0] + dir[0], robot[1] + dir[1])

total = 0  
for y in range(len(grid)):
    print("".join(grid[y]))
    for x in range(len(grid[y])):
        if grid[y][x] == "O":
            total += 100 * y + x

print(total)
