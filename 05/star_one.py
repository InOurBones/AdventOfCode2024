with open("./05/input.txt", "r") as file:
    rule_list, pages = [x.split("\n") for x in file.read().split("\n\n")]

# key cannot be before value
rules: dict[int, set] = {}
for x, y in [map(int, rule.split("|")) for rule in rule_list]:
    if y not in rules:
        rules[y] = set()
    
    rules[y].add(x)

def is_valid(page, rules) -> bool:
    for i, val in enumerate(page[:-1]):
        if val not in rules:
            continue

        if set(page[i + 1:]).intersection(rules[val]) != set():
            return False
    return True

total = 0
for page in [list(map(int, p.split(","))) for p in pages]:
    if is_valid(page, rules):
        total += page[int(len(page)/2)]

print(total)
