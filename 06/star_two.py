from copy import deepcopy
with open("./06/input.txt", "r") as file:
    input = [list(x) for x in file.read().split("\n")]

length = len(input)
width = len(input[0])

def get_start_coords(input) -> {int, int}:
    for y in range(length):
        for x in range(width):
            if input[y][x] == "^":
                return x, y
    return -1, -1

def mark_path(inp: list[str], start_x: int, start_y: int) -> tuple[list[str], bool]:
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    cur_dir = 0
    dir_x, dir_y = dirs[cur_dir]
    cur_x = start_x
    cur_y = start_y
    wall_count = 0
    while True:
        next_y = cur_y + dir_y
        next_x = cur_x + dir_x
                
        if inp[cur_y][cur_x] != "X":
            wall_count = 0
        inp[cur_y][cur_x] = "X"

        if next_y in (-1, length) or next_x in (-1, width):
            return inp, False

        next_val = inp[next_y][next_x]
        if next_val == "#":
            wall_count += 1
            if wall_count == 4:
                return inp, True

            cur_dir = (cur_dir + 1 ) % 4
            dir_x, dir_y = dirs[cur_dir]
            continue

        cur_x = next_x
        cur_y = next_y

start_x, start_y = get_start_coords(input)
marked_input, _ = mark_path(deepcopy(input), start_x, start_y)

all_coords = []
for y in range(length):
    for x in range(width):
        if marked_input[y][x] == "X":
            all_coords.append((x, y))

total = 0
for obst_x, obst_y in all_coords:
    input_copy = deepcopy(input)
    input_copy[obst_y][obst_x] = "#"
    _, has_loop = mark_path(input_copy, start_x, start_y)
    if has_loop:
        total += 1

print(total)
