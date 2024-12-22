with open("./14/input.txt", "r") as file:
    input = file.read().split("\n")
    
map_width = 101
map_length = 103


for seconds in range(10_000):
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

    mapje = [["."] * map_width for _ in range(map_length)]
    for drone in drones:
        px, py = drone
        mapje[py][px] = "#"

    for line in mapje:
        if "".join(line).count("#") > 30:
            for line in mapje:
                print("".join(line))
            print(seconds)
