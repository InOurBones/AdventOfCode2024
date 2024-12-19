with open("./10/dummy.txt", "r") as file:
    input = [list(map(int, x)) for x in file.read().split("\n")]

trailheads = []
for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] == 0:
            trailheads.append((x, y))

def paths_around(x, y) -> set[tuple[int, int]]:
    own_height = input[y][x]
    result = set()
    to_check = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]

    for x, y in to_check:
        try:
            if own_height - 1 <= input[y][x] <= own_height + 1:
                result.add((x, y))
        except IndexError:
            pass
    return result

for x, y in trailheads:
    total = 0
    paths_found = set()
    paths_to_check = paths_around(x, y)
    while not paths_to_check.issubset(paths_found):
        path = paths_to_check.pop()
        if path in paths_found:
            continue
        if input[path[1]][path[0]] == 9:
            total += 1
        paths_found.add(path)
        paths_to_check = paths_to_check.union(paths_around(*path))
    print(total)
