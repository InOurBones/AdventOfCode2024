with open("./12/input.txt", "r") as file:
    input = [list(x) for x in file.read().split("\n")]

def needs_fence(input: list[list[str]], plant: str, x: int, y: int) -> bool:
    if -1 in (x, y):
        return True
    if y == len(input):
        return True
    if x == len(input[0]):
        return True
    return input[y][x] != plant

def get_region(input: list[list[str]], x: int, y: int) -> tuple[list[set[int]], int]:
    plant = input[y][x]
    visited = set()
    fence_count = 0
    plants_to_check = [(x, y)]
    while plants_to_check:
        x, y = plants_to_check.pop()
        
        if (x, y) in visited:
            continue

        if needs_fence(input, plant, x, y):
            fence_count += 1
            continue

        visited.add((x, y))
        for new_x, new_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if (new_x, new_y) not in visited:
                plants_to_check.append((new_x, new_y))
    
    return visited, len(visited) * fence_count

total = 0
visited: set[set[int]] = set()
for y in range(len(input)):
    for x in range(len(input[0])):
        if (x, y) in visited:
            continue

        region, cost = get_region(input, x, y)
        visited |= region
        total += cost

print(total)
