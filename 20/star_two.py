with open("./20/input.txt", "r") as file:
    grid = [list(x) for x in file.read().split("\n")]

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "S":
            start = (x, y)
        elif grid[y][x] == "E":
            end = (x, y)

queue = [(start[0], start[1], 0, dict())]
while queue:
    x, y, time, visited = queue.pop(0)
    visited[(x, y)] = time

    if (x, y) == end:
        break

    for new_x, new_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if -1 not in (new_x, new_y) and (new_x, new_y) not in visited and grid[new_y][new_x] != "#":
            queue.append((new_x, new_y, time + 1, visited.copy()))

total = 0
threshold = 100
path = sorted(visited, key=visited.get)
for time2 in range(threshold, len(path)):
    for time1 in range(time2 - threshold):
        x1, y1 = path[time1]
        x2, y2 = path[time2]
        distance = abs(x1 - x2) + abs(y1 - y2)
        if distance <= 20 and time2 - time1 - distance >= threshold:
            total += 1

print(total)
