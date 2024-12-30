with open("./20/input.txt", "r") as file:
    grid = [list(x) for x in file.read().split("\n")]

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "S":
            start = (x, y)
        elif grid[y][x] == "E":
            end = (x, y)

visited = dict()
queue = [(start[0], start[1], 0, dict())]
while queue:
    x, y, time, visited = queue.pop(0)
    visited[(x, y)] = time

    if (x, y) == end:
        break

    for new_x, new_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if -1 not in [new_x, new_y] and (new_x, new_y) not in visited and grid[new_y][new_x] != "#":
            queue.append((new_x, new_y, time + 1, visited.copy()))

total = 0
for (x, y), time in visited.items():
    for new_x, new_y in [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]:
        if visited.get((new_x, new_y), 0) - time >= 102:
            total += 1

print(total)
