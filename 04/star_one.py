with open("./04/input.txt", "r") as file:
    input = file.read().split("\n")

def count_horizontal(input: str) -> int:
    full_input = "-".join(input)
    return full_input.count("XMAS") + full_input.count("SAMX")

def count_vertical(input: str) -> int:
    full_input = ["".join([row[i] for row in input]) for i in range(len(input[0]))]
    return count_horizontal(full_input)

def count_diagonal(input: str) -> int:
    result = 0
    for inp in (input, list(reversed(input))):
        full_input = [[] for _ in range(len(inp) * 2 - 1)]
        for i in range(len(inp)):
            for j, char in enumerate(inp[i]):
                full_input[i+j].append(char)
        result += count_horizontal(["".join(x) for x in full_input])
    return result

total = count_horizontal(input) + count_vertical(input) + count_diagonal(input)
print(total)
