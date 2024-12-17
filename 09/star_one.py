with open("./09/input.txt", "r") as file:
    input = list(map(int, file.read() + "0")) # lazy cheat

disk = []
for i in range(0,len(input),2):
    file_size, free_space = input[i:i+2]
    file_id = int(i/2)
    
    disk.extend([str(file_id)] * file_size + ["."] * free_space)

try:
    while True:
        left_idx = disk.index(".")
        right_value = disk.pop()
        if right_value != ".":
            disk[left_idx] = right_value
except ValueError:
    pass

total = 0
for i in range(len(disk)):
    total += int(disk[i]) * i
print(total)