from functools import cache


with open("./21/input.txt", "r") as file:
    codes = file.read().split("\n")

numpad  = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
                 '0': (3, 1), 'A': (3, 2),
}
dirpad = {
                 '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2),
}

def get_combinations(keypad: dict[str, tuple[int, int]], empty_coords: tuple[int, int]) -> dict[tuple[int, int], str]:
    sequence = dict()
    for a, (x1, y1) in keypad.items():
        for b, (x2, y2) in keypad.items():
            path = "<" * (y1 - y2) + "v" * (x2 - x1) + "^" * (x1 - x2) + ">" * (y2 - y1)
            if empty_coords == (x1, y2) or empty_coords == (x2, y1):
                path = path[::-1]
            sequence[(a, b)] = path + "A"
    return sequence

numpad_combinations = get_combinations(numpad, (3, 0))
dirpad_combinations = get_combinations(dirpad, (0, 0))

@cache
def get_length(sequence: str, iterations, first_iter = False) -> str:
    if iterations == 0:
        return len(sequence)
    prev = "A"
    total = 0
    combinations = numpad_combinations if first_iter else dirpad_combinations
    for char in sequence:
        total += get_length(combinations[(prev, char)], iterations - 1)
        prev = char
    return total

total = 0
for code in codes:
    total += int(code[:-1]) * get_length(code, 26, True)

print(total)
