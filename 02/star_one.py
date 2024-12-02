
def is_safe(levels: list[int]) -> bool:
    direction = (-1, 1)[levels[0] > levels[1]]
    prev = levels[0]
    for cur in levels[1:]:
        diff = (prev - cur) * direction
        if diff > 3 or diff <= 0:
            return False
        prev = cur
    return True

total = 0
with open("./02/input.txt", "r") as file:
    for line in [x.replace("\n", "") for x in file.readlines()]:
        levels = [int(x) for x in line.split(" ")]
        total += int(is_safe(levels))
print(total)
