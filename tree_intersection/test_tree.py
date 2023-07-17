import pytest
from tree_intersection.tree_intersection import tree_intersection
from Tree.Node import Node
from Tree.Tree import Tree
@pytest.fixture
def setup_trees():
    node1 = Node(1)
    node0 = Node(0)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1.left = node0
    node0.left = node2
    node1.right = node3
    node0.right = node4
    node3.right = node5
    first_tree = Tree()
    first_tree.root = node1
    
    node_2 = Node(2)
    node_5 = Node(5)
    node_10 = Node(10)
    node_20 = Node(20)
    node_10.left = node_5
    node_5.left = node_2
    node_10.right = node_20
    second_tree = Tree()
    second_tree.root = node_10
    
    return first_tree, second_tree

def test_1(setup_trees):
    first_tree, second_tree = setup_trees
    assert {2, 5} == tree_intersection(first_tree, second_tree)

def test_2(setup_trees):
    first_tree, second_tree = setup_trees
    fifth_tree = Tree()
    assert "Empty Trees" == tree_intersection(first_tree, fifth_tree)
def test_3(setup_trees):
    first_tree, second_tree = setup_trees
    node_15 = Node(15)
    node_5 = Node(5)
    node_8 = Node(8)
    node_15.left = node_5
    node_15.right = node_8
    third_tree = Tree()
    third_tree.root = node_15
    assert {5} == tree_intersection(second_tree, third_tree)
