
def is_safe(levels: list[int]) -> bool:
    if levels not in [sorted(levels), sorted(levels)[::-1]]:
        return False
    for i in range(1, len(levels)):
        if abs(levels[i] - levels[i - 1]) not in [1, 2, 3]:
            return False
    return True

def is_dampened_safe(levels: list[int]) -> bool:
    return any(is_safe(levels[:i] + levels[i + 1 :]) for i in range(len(levels)))

total = 0
with open("./02/input.txt", "r") as file:
    for line in [x.replace("\n", "") for x in file.readlines()]:
        levels = list(map(int, line.split(" ")))
        total += int(is_dampened_safe(levels))
print(total)
