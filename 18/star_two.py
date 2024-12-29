from typing import Generator

with open("./18/input.txt", "r") as file:
    input = [(int(z.split(",")[0]), int(z.split(",")[1])) for z in file.read().split("\n")]

size = 71
bytes_to_sim = 1024
grid = [["."] * size for _ in range(size)]

def get_neighbours(grid: list[list[str]], visited: set[tuple[int, int]], x: int, y: int) -> Generator:
    for new_x, new_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if new_x >= 0 and new_y >= 0 \
        and new_x < size and new_y < size \
        and grid[new_y][new_x] == "." \
        and (new_x, new_y) not in visited:
            yield new_x, new_y

def get_path(grid) -> list[tuple[int, int]]:
    neighbours_to_check = [(0, 0, list())]
    visited = set()
    while neighbours_to_check:
        x, y, path = neighbours_to_check.pop(0)
        if x == y == size - 1:
            return path
        
        for new_x, new_y in get_neighbours(grid, visited, x, y):
            neighbours_to_check.append((new_x, new_y, path + [(new_x, new_y)]))
            visited.add((new_x, new_y))
    return

total = None
path = None
for i, (x, y) in enumerate(input):
    grid[y][x] = "#"
    if i > bytes_to_sim and (path is None or (x, y) in path):
        path = get_path(grid)
        if path is None:
            total = f"{x},{y}"
            break

print(total)     
    