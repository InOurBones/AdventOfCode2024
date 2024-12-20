def kaas(x):
    return "." if x == "." else int(x)

with open("./10/input.txt", "r") as file:
    input = [list(map(kaas, x)) for x in file.read().split("\n")]

trailheads = []
for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] == 0:
            trailheads.append((x, y))

def paths_around(x, y) -> list[tuple[int, int]]:
    own_height = input[y][x]
    result = []
    to_check = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]

    for x, y in to_check:
        try:
            if -1 not in (x, y) and input[y][x] == own_height + 1:
                result.append((x, y))
        except IndexError:
            pass
    return result

total = 0
for x, y in trailheads:
    paths_found = []
    paths_to_check = paths_around(x, y)
    while paths_to_check:
        path = paths_to_check.pop()
        if input[path[1]][path[0]] == 9:
            total += 1
        paths_found.append(path)
        paths_to_check = paths_to_check + paths_around(*path)

print(total)
