from graph.graph import *

graph1 = Graph()

a = graph1.add_node("A")
b = graph1.add_node("B")
c = graph1.add_node("C")
d = graph1.add_node("D")
# a = graph1.add_node("5")
# b = graph1.add_node("3")
# c = graph1.add_node("4")
# d = graph1.add_node("1")
g = graph1.add_node("G")
h = graph1.add_node("H")
e = graph1.add_node("E")
f = graph1.add_node("F")

graph1.add_edge(a,b)
graph1.add_edge(a,d)
graph1.add_edge(b,a)
graph1.add_edge(b,d)
graph1.add_edge(b,c)
graph1.add_edge(c,b)
graph1.add_edge(c,g)
graph1.add_edge(d,a)
graph1.add_edge(d,b)
graph1.add_edge(d,e)
graph1.add_edge(d,h)
graph1.add_edge(d,f)
graph1.add_edge(e,d)
graph1.add_edge(h,d)
graph1.add_edge(h,f)
graph1.add_edge(f,d)
graph1.add_edge(f,h)
# print(graph1.neighbors(a))
# print(graph1.size)
# print(graph1.vertices())
# print(graph1.breadth_first(d))
print(graph1.Depth_first(a))
vertices = ["a", "b", "c", "d", "e"]
edges = [
        [False, True, False, False, True],
        [True, False, True, True, False],
        [False, True, False, True, False],
        [False, True, True, False, True],
        [True, False, False, True, False],
    ]
print(graph1.create_adjacency_list(vertices,edges))

