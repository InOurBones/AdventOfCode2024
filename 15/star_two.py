with open("./15/input.txt", "r") as file:
    grid_raw, steps = file.read().split("\n\n")
grid_changes = {
    "#": "##",
    "O": "[]",
    ".": "..",
    "@": "@."
}
grid = []
for line in grid_raw.split("\n"):
    result = []
    for char in line:
        result.append(grid_changes[char])
    grid.append(list("".join(result)))

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

def box_to_move(grid: list[list[str]], x: int, y: int, dir: tuple[int, int]) -> set:
    char = (x, y)
    other_char = ((x-1, y), (x+1, y))[grid[y][x] == "["]

    char_new = tuple(map(add_num, char, dir))
    other_char_new = tuple(map(add_num, other_char, dir))

    if grid[char_new[1]][char_new[0]] != "#" and grid[other_char_new[1]][other_char_new[0]] != "#":
        return set([char, other_char])
    return []
    
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
    
    # grid[new_y][new_x] in ("[", "]")
    boxes_to_check = [(new_x, new_y)]
    boxes_to_move = set()
    while boxes_to_check:
        x, y = boxes_to_check.pop(0)
        boxes_found = box_to_move(grid, x, y, dir)
        if len(boxes_found) != 2:
            boxes_to_move = set()
            break
        boxes_to_move |= boxes_found
        for box in boxes_found:
            new_x, new_y = tuple(map(add_num, box, dir))
            if grid[new_y][new_x] in ("[", "]") and (new_x, new_y) not in boxes_to_move:
                boxes_to_check.append((new_x, new_y))

    boxes_to_move = sorted(list(boxes_to_move), reverse = dir[0] + dir[1] == 1)
    if not boxes_to_move:
        continue

    while boxes_to_move:
        box = boxes_to_move.pop(0)
        new_x, new_y = tuple(map(add_num, box, dir))
        grid[new_y][new_x] = grid[box[1]][box[0]]
        grid[box[1]][box[0]] = "."

    grid[robot[1] + dir[1]][robot[0] + dir[0]] = "@"
    grid[robot[1]][robot[0]] = "."
    robot = (robot[0] + dir[0], robot[1] + dir[1])

total = 0  
for y in range(len(grid)):
    print("".join(grid[y]))
    for x in range(len(grid[y])):
        if grid[y][x] == "[":
            total += 100 * y + x

print(total)
