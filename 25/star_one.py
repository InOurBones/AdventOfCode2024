
with open("./25/input.txt", "r") as file:
    schematics = file.read().split("\n\n")

locks, keys = [], []
for schematic in schematics:
    cur = {i for i, c in enumerate(schematic) if c == "#"}
    if schematic.startswith("#####"):
        locks.append(cur)
    else:
        keys.append(cur)

total = sum(not lock & key for lock in locks for key in keys)
print(total)
