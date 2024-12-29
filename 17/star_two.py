from copy import copy


with open("./17/input.txt", "r") as file:
    registers, instructions = file.read().split("\n\n")

registers = {key[0]: int(value) for _, key, value in [x.split(" ") for x in registers.split("\n")]}
instructions = list(map(int, instructions.split(" ")[1].split(",")))

def get_operand(registers: dict, inp: str) -> int:
    inp = int(inp)
    match inp:
        case _ if inp <= 3:
            return inp
        case 4:
            return registers["A"]
        case 5:
            return registers["B"]
        case 6:
            return registers["C"]

def get_output(registers, instructions):
    output = []
    i = 0
    while i < len(instructions) - 1:
        opcode, literal_operand = instructions[i:i+2]
        operand = get_operand(registers, literal_operand)
        i += 2
        match opcode:
            case 0:
                registers["A"] = registers["A"] // (2**operand)
            case 1:
                registers["B"] ^= literal_operand
            case 2:
                registers["B"] = operand % 8
            case 3:
                if registers["A"] != 0:
                    i = literal_operand
            case 4:
                registers["B"] ^= registers["C"]
            case 5:
                output.append(operand % 8)
            case 6:
                registers["B"] = registers["A"] // (2**operand)
            case 7:
                registers["C"] = registers["A"] // (2**operand)
    return output

A = 0
for i in reversed(range(len(instructions))):
    A <<= 3
    while get_output(copy(registers), instructions) != instructions[i:]:
        A += 1

print(A)
