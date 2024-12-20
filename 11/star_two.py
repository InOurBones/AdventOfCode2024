with open("./11/input.txt", "r") as file:
    input = list(map(int, file.read().split(" ")))

blink_amount = 75
for _ in range(blink_amount):
    result = []
    for x in input:
        if x == 0:
            result.append(1)
        elif x >= 10 and len(str(x)) % 2 == 0:
            half = int(len(str(x))/2)
            result.append(int(str(x)[:half]))
            result.append(int(str(x)[half:]))
        else:
            result.append(x * 2024)
    input = result
total = len(result)
print(total)
