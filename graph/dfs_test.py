import pytest

from graph.graph import Graph
def test_graph_depth_first():
    graph1 = Graph()
    a = graph1.add_node("5")
    b = graph1.add_node("3")
    c = graph1.add_node("4")
    d = graph1.add_node("1")

    graph1.add_edge(a,b)
    graph1.add_edge(a,c)
    graph1.add_edge(a,d)
    graph1.add_edge(c,b)
    graph1.add_edge(d,b)
    graph1.add_edge(d,c)

    assert graph1.Depth_first(a) == ['5', '1', '4', '3']
def test_depth_first():
    graph1 = Graph()
    a = graph1.add_node("5")
    b = graph1.add_node("3")
    c = graph1.add_node("4")
    d = graph1.add_node("1")

    graph1.add_edge(a,b)
    graph1.add_edge(a,c)
    graph1.add_edge(a,d)
    graph1.add_edge(c,b)
    graph1.add_edge(d,b)
    graph1.add_edge(d,c)

    assert graph1.Depth_first(c) == ['4', '1', '3', '5']
    
def test_depth_first3():
    graph1 = Graph()
    a = graph1.add_node("5")
    b = graph1.add_node("3")
    c = graph1.add_node("4")
    d = graph1.add_node("1")

    graph1.add_edge(a,b)
    graph1.add_edge(a,c)
    graph1.add_edge(a,d)
    graph1.add_edge(c,b)
    graph1.add_edge(d,b)
    graph1.add_edge(d,c)

    assert graph1.Depth_first(4) == []