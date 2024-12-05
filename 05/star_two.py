with open("./05/input.txt", "r") as file:
    rule_list, pages = [x.split("\n") for x in file.read().split("\n\n")]

rules: dict[int, set] = {}
for x, y in [map(int, rule.split("|")) for rule in rule_list]:
    if x not in rules:
        rules[x] = set()
    
    rules[x].add(y)

def sort_page(page, rules) -> list[int]:
    page = list(reversed(page))
    i = 0
    while i < len(page):
        val = page[i]
        if val not in rules:
            i += 1
            continue

        if set(page[i + 1:]).intersection(rules[val]) != set():
            has_changed = False
            for j in range(1, len(page)):
                if set(page[i+j:]).intersection(rules[val]) == set():
                    page.insert(i+j-1, page.pop(i))
                    i -= 1
                    has_changed = True
                    break
            if not has_changed: # didnt change
                page.append(page.pop(0))
                i -= 1
        i += 1
    return list(reversed(page))

total = 0
for page in [list(map(int, p.split(","))) for p in pages]:
    sorted_page = sort_page(page, rules)
    if page != sorted_page:
        total += sorted_page[int(len(page)/2)]
print(total)