with open("./22/input.txt", "r") as file:
    input = map(int, file.read().split("\n"))

def calc_num(num: int) -> int:
    num = ((num * 64) ^ num) % 16777216
    num = (int(num / 32) ^ num) % 16777216
    num = ((num * 2048) ^ num) % 16777216
    return num

total = 0
for num in input:
    for _ in range(2000):
        num = calc_num(num)
    total += num

print(total)
