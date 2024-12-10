import itertools

with open("./07/input.txt", "r") as file:
    input = file.read().split("\n")
    input = [(int(x.split(": ")[0]), list(map(int, x.split(": ")[1].split(" ")))) for x in input]

total = 0
for res, nums in input:
    for x in map(''.join, itertools.product('01', repeat=len(nums) - 1)):
        nums_copy = nums.copy()
        start = nums_copy.pop(0)
        for oper in x:
            if oper == "0":
                start += nums_copy.pop(0)
            elif oper == "1":
                start *= nums_copy.pop(0)
            if start > res:
                break
        if start == res:
            total += res
            break

print(total)