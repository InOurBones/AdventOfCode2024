from collections import deque
import networkx as nx

with open("./24/input.txt", "r") as file:
    wires, gates = file.read().split("\n\n")

graph = nx.DiGraph()
for wire in wires.split("\n"):
    name, value = wire.split(": ")
    graph.add_node(name, v = int(value))

for gate in gates.split("\n"):
    a, op, b, _, c = gate.split()
    graph.add_edge(a, c, op=op)
    graph.add_edge(b, c, op=op)

values = nx.get_node_attributes(graph, "v") 
queue = deque(values)
while queue:
    key = queue.popleft()
    for s in graph.successors(key):
        if s in values:
            continue
        a, b = graph.predecessors(s)
        op = graph[a][s]["op"]
        if a in values and b in values:
            a = values[a]
            b = values[b]
            match op:
                case "XOR":
                    values[s] = a ^ b
                case "OR":
                    values[s] = a | b
                case "AND":
                    values[s] = a & b
            queue.append(s)
            
total = int(''.join(map(lambda k: str(values[k]), sorted([x for x in values if x[0] == 'z'], reverse=True))), 2)
print(total)
