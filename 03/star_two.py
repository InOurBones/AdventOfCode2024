import re
rgx = re.compile(r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))")

with open("./03/input.txt", "r") as file:
    input = file.read()

total = 0
is_enabled = True
for x in rgx.finditer(input):
    if "do" in x.group():
        is_enabled = "don't" not in x.group()
        continue
    
    if is_enabled:
        left, right = x.group()[4:-1].split(",")
        total += (int(left) * int(right))
print(total)
