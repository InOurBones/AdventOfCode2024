with open("./14/input.txt", "r") as file:
    input = file.read().split("\n")
    
map_width = 101
map_length = 103
seconds = 100

drones = []
for drone in input:
    p, v = drone.split(" ")
    px, py = map(int, p[2:].split(","))
    vx, vy = map(int, v[2:].split(","))

    new_x = (px + vx * seconds) % map_width
    if new_x < 0:
        new_x += map_width
    new_y = (py + vy * seconds) % map_length
    if new_y < 0:
        new_y += map_length
    drones.append((new_x, new_y))

quadrants = [0, 0, 0, 0]
for drone in drones:
    x, y = drone
    half_map_width = int(map_width / 2)
    half_map_length = int(map_length / 2)
    if x < half_map_width and y < half_map_length:
        quadrants[0] += 1
    if x > half_map_width and y < half_map_length:
        quadrants[1] += 1
    if x < half_map_width and y > half_map_length:
        quadrants[2] += 1
    if x > half_map_width and y > half_map_length:
        quadrants[3] += 1

total = quadrants.pop()
for count in quadrants:
    total *= count
print(total)
