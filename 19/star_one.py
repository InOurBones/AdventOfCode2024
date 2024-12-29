from functools import cache

with open("./19/input.txt", "r") as file:
    towels, designs = file.read().split("\n\n")
towels = tuple(towels.split(", "))
designs = designs.split("\n")

@cache
def is_possible(design, towels):
    if not design:
        return 1
    
    return sum(is_possible(design[len(towel):], towels)
               for towel in towels if design.startswith(towel))

possible = [is_possible(design, towels) for design in designs]
total = sum(map(bool, possible))
print(total)
