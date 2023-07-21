from graph.graph import Graph

graph1 = Graph()

a = graph1.add_node("A")
b = graph1.add_node("B")
c = graph1.add_node("C")
d = graph1.add_node("D")
five = graph1.add_node("5")
two = graph1.add_node("2")
four = graph1.add_node("4")
three = graph1.add_node("3")
one = graph1.add_node("1")


# graph1.add_edge(a,b)
# graph1.add_edge(a,c)
# graph1.add_edge(c,b)
# graph1.add_edge(d,b)
# graph1.add_edge(d,c)
# graph1.add_edge(five, two)
# graph1.add_edge(four, five)
# graph1.add_edge(four, one)
# graph1.add_edge(two, three)
# graph1.add_edge(three, one)
print(graph1)
node_to_start_from = two
result = graph1.breadth_first(node_to_start_from)

print("Breadth-First Search Result:")
print(result)