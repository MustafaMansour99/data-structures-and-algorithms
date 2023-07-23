import pytest   
from graph.graph import Graph

def test1():
    gph = Graph()
    gph.add_node("A")
    actual = str(gph)

    expected = 'A -> \n'
    assert actual == expected

def test2():
    graph = Graph()

    a = graph.add_node("A")
    b = graph.add_node("B")
    graph.add_edge(a,b)
    actual = str(graph)
    expected = "A -> B -----> \nB -> A -----> \n"
    assert actual == expected

def test3():
    """A collection of all vertices can be properly retrieved from the graph"""
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    expected = ['A', 'B', 'C', 'D']
    actual=graph.vertices()
    assert actual == expected
def test4():
    """All appropriate neighbors can be retrieved from the graph"""
    graph = Graph()
    a = graph.add_node("A")
    b = graph.add_node("B")
    c = graph.add_node("C")
    d = graph.add_node("D")
    graph.add_edge(a,b)
    graph.add_edge(a,c)
    graph.add_edge(a,d)
    graph.add_edge(c,b)
    graph.add_edge(d,b)
    graph.add_edge(d,c)
    actual=graph.neighbors(a)
    expected = "B--->C--->D--->"
    assert actual == expected
def test5():
    graph = Graph()
    a = graph.add_node("A")
    b = graph.add_node("B")
    c = graph.add_node("C")
    d = graph.add_node("D")
    graph.add_edge(a,b)
    graph.add_edge(a,c)
    graph.add_edge(a,d)
    graph.add_edge(c,b)
    graph.add_edge(d,b)
    graph.add_edge(d,c)
    actual=graph.size
    expected =4
    assert actual == expected
def test6():
    graph = Graph()

    a = graph.add_node("A")

    graph.add_edge(a,None)
    actual = str(graph)
    expected ="A -> \n"
    assert actual == expected
