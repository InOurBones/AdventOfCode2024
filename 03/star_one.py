import re
rgx = re.compile(r"mul\(\d{1,3},\d{1,3}\)")

with open("./03/input.txt", "r") as file:
    input = file.read()

total = 0
for x in rgx.finditer(input):
    left, right = x.group()[4:-1].split(",")
    total += (int(left) * int(right))
print(total)
