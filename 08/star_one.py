import itertools
import operator

with open("./08/input.txt", "r") as file:
    input = [list(x) for x in file.read().split("\n")]

nodes = {}
for y in range(len(input)):
    for x in range(len(input[0])):
        elem = input[y][x]
        if elem == ".":
            continue

        if elem not in nodes:
            nodes[elem] = []
        nodes[elem].append((x, y))

def in_bounds(inp: list[str], coords: tuple[int, int]) -> bool:
    x, y = coords
    if x < 0 or x >= len(inp[0]):
        return False
    if y < 0 or y >= len(inp):
        return False
    return True

for node, coords in nodes.items():
    for left, right in itertools.combinations(coords, r = 2):
        diff = tuple(map(operator.sub, left, right))
        left = tuple(map(operator.add, left, diff))
        right = tuple(map(operator.sub, right, diff))

        if in_bounds(input, left) and input[left[1]][left[0]] != "#":
            input[left[1]][left[0]] = "#"

        if in_bounds(input, right) and input[right[1]][right[0]] != "#":
            input[right[1]][right[0]] = "#"

total = "".join("".join(x) for x in input).count("#")
print(total)
