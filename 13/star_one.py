with open("./13/input.txt", "r") as file:
    input = file.read().split("\n\n")

def get_coords(line: str) -> tuple[int, int]:
    x_idx = line.find("X")
    space_idx = line.find(" ", x_idx)
    y_idx = line.find("Y", space_idx)
    return int(line[x_idx+2:space_idx-1]), int(line[y_idx+2:])

total = 0
for machine in input:
    (ax, ay), (bx, by), (px, py) = map(get_coords, machine.split("\n"))
    t1 = bx*py-by*px
    t2 = bx*ay-by*ax
    if t1 % t2:
        continue
    a_pressed = t1//t2
    t3 = px - ax * a_pressed
    if t3 % bx:
        continue
    b_pressed = t3 // bx
    total += a_pressed * 3 + b_pressed
print(total)
