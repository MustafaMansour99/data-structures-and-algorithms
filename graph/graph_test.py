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