from graph.graph import *

graph1 = Graph()

a = graph1.add_node("A")
b = graph1.add_node("B")
c = graph1.add_node("C")
d = graph1.add_node("D")

graph1.add_edge(a,b)
graph1.add_edge(a,c)
graph1.add_edge(a,d)
graph1.add_edge(c,b)
graph1.add_edge(d,b)
graph1.add_edge(d,c)
print(graph1.neighbors(a))
print(graph1.size)
print(graph1.vertices())
print(graph1.breadth_first(d))

print(graph1)