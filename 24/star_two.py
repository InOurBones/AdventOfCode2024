with open("./24/input.txt", "r") as file:
    wires, gates = file.read().split("\n\n")

XOR = 'XOR'
AND = 'AND'
OR = 'OR'

graph: dict[tuple[str, str, str], str] = dict()
reversed_graph: dict[str, tuple[str, str, str]] = dict()
for gate in gates.split("\n"):
    a, op, b, _, c = gate.split()
    a, b = min(a, b), max(a, b)
    graph[a, b, op] = c
    reversed_graph[c] = a, b, op

def swap(a, b):
    reversed_graph[a], reversed_graph[b] = reversed_graph[b], reversed_graph[a]
    graph[reversed_graph[a]], graph[reversed_graph[b]] = graph[reversed_graph[b]], graph[reversed_graph[a]]

total = set()
c = ""
for i in range(int(max(reversed_graph)[1:])):
    x = f"x{i:02}"
    y = f"y{i:02}"
    z = f"z{i:02}"
    zn = f"z{i + 1:02}"
    xxy = graph[x, y, XOR]
    xay = graph[x, y, AND]
    if not c:
        c = xay
        continue

    a, b = min(c, xxy), max(c, xxy)
    key = a, b, XOR
    if key not in graph:
        a, b = list(set(reversed_graph[z][:2]) ^set(key[:2]))
        total.add(a)
        total.add(b)
        swap(a, b)
    elif graph[key] != z:
        total.add(graph[key])
        total.add(z)
        swap(z, graph[key])
    
    key = reversed_graph[z]
    xxy = graph[x, y, XOR]
    xay = graph[x, y, AND]
    c = graph[min(c, xxy), max(c, xxy), AND]
    c = graph[min(c, xay), max(c, xay), OR]

print(",".join(sorted(total)))
