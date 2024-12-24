from enum import Enum
import sys
from collections import deque

with open("./16/input.txt", "r") as file:
    input = [list(x) for x in file.read().split("\n")]
    input[len(input) - 2][1] = 0

class Direction(Enum):
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)

def turn(dir: Direction, turn_dir: str) -> Direction:
    dir_list = list(Direction)
    dir_idx = dir_list.index(dir)
    turn_dir = dir_idx + (-1, 1)[turn_dir == "right"]
    return dir_list[turn_dir % len(dir_list)]
        
def get_neighbours(pos: tuple[int, int, Direction]) -> list[tuple[int, int, Direction]]:
    x, y, dir = pos
    forward = (x + dir.value[0], y + dir.value[1], dir)
    left = (x, y, turn(dir, "left"))
    right = (x, y, turn(dir, "right"))
    return [forward, left, right]

dist = {
    (x, y, d): sys.maxsize
    for x in range(len(input[0]))
    for y in range(len(input))
    for d in [Direction.EAST, Direction.NORTH, Direction.WEST, Direction.SOUTH]
}
dist[(1, len(input) - 2, Direction.EAST)] = 0

visited = {
    (x, y, d): False
    for x in range(len(input[0]))
    for y in range(len(input))
    for d in [Direction.EAST, Direction.NORTH, Direction.WEST, Direction.SOUTH]
}

pred = {
    (x, y, d): None
    for x in range(len(input[0]))
    for y in range(len(input))
    for d in [Direction.EAST, Direction.NORTH, Direction.WEST, Direction.SOUTH]
}
pred[(1, len(input) - 2, Direction.EAST)] = []

q = [(1, len(input) - 2, Direction.EAST)]
while len(q) > 0:
    pos = q.pop(0)
    neighbors = get_neighbours(pos)
    neighbors.sort(key=lambda n: dist[n])
    for n in neighbors:
        if visited[n] or input[n[1]][n[0]] == '#':
            continue
        if n not in q and input[n[1]][n[0]] != 'E':
            q.append(n)
        d = dist[pos]
        if pos[0] == n[0] and pos[1] == n[1]:
            d += 1000
        else:
            d += 1
        if d < dist[n]:
            dist[n] = d
            pred[n] = [pos]
        elif d == dist[n]:
            pred[n].append(pos)
    visited[pos] = True
    q.sort(key=lambda n: dist[n])

end_1 = (len(input[0]) - 2, 1, Direction.EAST)
end_2 = (len(input[0]) - 2, 1, Direction.NORTH)

end_dist_1 = dist[end_1]
end_dist_2 = dist[end_2]

q = deque()
if end_dist_1 <= end_dist_2:
    q.append(end_1)
if end_dist_1 >= end_dist_2:
    q.append(end_2)

tiles = set()
while len(q) != 0:
    p = q.popleft()
    tiles.add(p[:2])
    for v in pred[p]:
        q.append(v)

total = len(tiles)
print(total)
