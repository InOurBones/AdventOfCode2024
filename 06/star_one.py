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

def mark_path(input: list[str], start_x: int, start_y: int) -> list[str]:
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    cur_dir = 0
    dir_x, dir_y = dirs[cur_dir]
    cur_x = start_x
    cur_y = start_y
    while True:
        input[cur_y][cur_x] = "X"
        next_y = cur_y + dir_y
        next_x = cur_x + dir_x
        
        if next_y in (-1, length) or next_x in (-1, width):
            return input

        next_val = input[cur_y + dir_y][cur_x + dir_x]
        if next_val == "#":
            cur_dir = (cur_dir + 1 ) % 4
            dir_x, dir_y = dirs[cur_dir]
            continue

        cur_x = next_x
        cur_y = next_y

x, y = get_start_coords(input)
input = mark_path(input, x, y)
total = "".join(["".join(x) for x in input]).count("X")
print(total)
