from collections import defaultdict
import itertools

with open("./23/input.txt", "r") as file:
    input: list[tuple[str, str]] = [x.split("-") for x in file.read().split("\n")]

mapping = defaultdict(list)
for left, right in input:
    mapping[left].append(right)
    mapping[right].append(left)

keys_start_t = filter(lambda x: x.startswith("t"), mapping.keys())
result = set()
for key in keys_start_t:
    for left, right in itertools.combinations(mapping[key], 2):
        if right in mapping[left]:
            result.add(tuple(sorted([left, right, key])))
print(len(result))
