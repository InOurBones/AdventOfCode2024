left_list = {}
right_list = {}
with open("./01/input.txt", "r") as file:
    for line in [x.replace("\n", "") for x in file.readlines()]:
        left, right = line.split("   ")
        if left not in left_list:
            left_list[left] = 1
        else:
            left_list[left] += 1

        if right not in right_list:
            right_list[right] = 1
        else:
            right_list[right] += 1

total = 0
for key, value in left_list.items():
    total += (int(key) * value * right_list.get(key, 0))
print(total)
