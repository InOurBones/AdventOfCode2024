from collections import defaultdict

with open("./22/input.txt", "r") as file:
    input = map(int, file.read().split("\n"))

def calc_num(num: int) -> int:
    num = ((num * 64) ^ num) % 16777216
    num = (int(num / 32) ^ num) % 16777216
    num = ((num * 2048) ^ num) % 16777216
    return num

ranges = defaultdict(list)
for num in input:
    visited = set()
    changes = list()

    for _ in range(2000):
        next_num = calc_num(num)
        changes.append((next_num % 10) - (num % 10))
        num = next_num

        if len(changes) == 4:
            key = ",".join(map(str, changes))
            if key not in visited:
                ranges[key].append(num % 10)
                visited.add(key)
            changes.pop(0)

total = max(sum(val) for val in ranges.values())
print(total)
