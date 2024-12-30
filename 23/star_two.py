from collections import Counter, defaultdict

with open("./23/input.txt", "r") as file:
    input: list[tuple[str, str]] = [x.split("-") for x in file.read().split("\n")]

mapping = defaultdict(list)
for left, right in input:
    mapping[left].append(right)
    mapping[right].append(left)

network = list()
for k, v in mapping.items():
    sv = set(v)
    sv.add(k)
    network.append(sv)

count = Counter()
for i in range(len(network)):
    for j in range(i+1, len(network[1:])):
        left, right = network[i], network[j]
        if len(left & right) > 10:
            count[tuple(sorted(list(left & right)))] += 1

total = [k for k, v in count.items() if len(k) * (len(k) - 1) / 2 == v][0]
print(",".join(total))
