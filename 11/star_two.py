from collections import Counter

with open("./11/input.txt", "r") as file:
    input = Counter(map(int, file.read().split(" ")))

blink_amount = 75
for _ in range(blink_amount):
    result = Counter()
    for x, amount in input.items():
        if x == 0:
            result[1] += amount
        elif x >= 10 and len(str(x)) % 2 == 0:
            half = int(len(str(x))/2)
            result[int(str(x)[:half])] += amount
            result[int(str(x)[half:])] += amount
        else:
            result[x * 2024] += amount
    input = result
total = sum(input.values())
print(total)
