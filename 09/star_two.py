with open("./09/input.txt", "r") as file:
    input = list(map(int, file.read()))

file_sizes = input[::2]
files = [(i, file_sizes[i]) for i in range(len(file_sizes))]
free_space = input[1::2]

disk = []
for file, space in zip(files, free_space):
    disk.append(file)
    disk.append(space)
disk.append(files[-1])

for file_id, file_size in reversed(files):
    rel_idx = disk.index((file_id, file_size))

    space_idx = -1
    for i in range(rel_idx):
        if type(disk[i]) is int and disk[i] >= file_size:
            space_idx = i
            break
    
    if space_idx == -1:
        continue

    disk[space_idx] -= file_size
    disk[rel_idx - 1] += file_size
    del disk[rel_idx]
    disk.insert(space_idx, (file_id, file_size))
    disk.insert(space_idx, 0)

disk_sum = []
for x in disk:
    if type(x) is int:
        disk_sum.extend(["."] * x)
    else:
        disk_sum.extend([str(x[0])] * x[1])

total = 0
for i, val in enumerate(disk_sum):
    if val != ".":
        total += int(val) * i
print(total)