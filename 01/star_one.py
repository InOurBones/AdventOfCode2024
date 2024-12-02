left_list = []
right_list = []
with open("./01/input.txt", "r") as file:
    for line in file.readlines():
        left, right = line.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))

left_list = sorted(left_list)
right_list = sorted(right_list)

total = 0
for left, right in zip(left_list, right_list):
    total += abs(left - right)
print(total)
