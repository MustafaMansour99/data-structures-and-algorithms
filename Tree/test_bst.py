import pytest
from Tree.bts_tree import BinarySearchTree

def test_1():
    "Can successfully instantiate an empty tree"
    bst = BinarySearchTree()
    expected = "Tree is empty"
    actual = bst.is_empty()
    assert expected == actual
def test_2():
    "Can successfully instantiate a tree with a single root node"
    bst = BinarySearchTree()
    bst.add(1)
    expected = 1
    actual = bst.root.value
    assert expected == actual
def test_3():
    "Can successfully return a collection from a pre-order traversal"
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(2)
    bst.add(1)
    expected =[5, 2, 1]
    actual = bst.traverse_preorder(bst.root)
    assert expected == actual
    
def test_4():
    "Can successfully return a collection from a in-order traversal"
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(2)
    bst.add(1)
    expected =[1, 2, 5]
    actual = bst.traverse_inorder(bst.root)
    assert expected == actual
    
def test_5():
    "Can successfully return a collection from a post-order traversal"
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(2)
    bst.add(1)
    expected =[2, 1, 5]
    actual = bst.traverse_postorder(bst.root)
    assert expected == actual

def test_7():
    " can successfully check if value inside tree or not"
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(2)
    bst.add(1)
    expected = True
    actual = bst.contains(5)
    assert expected == actual
def test_8():
    " can successfully check if value inside tree or not"
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(2)
    bst.add(1)
    expected = False
    actual = bst.contains(7)
    assert expected == actual

def test_9():
    "Can successfully add child left and right"
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(2)
    bst.add(6)
    expected =[2, 6, 5]
    actual = bst.traverse_postorder(bst.root)
    assert expected == actual

def test_10():
    "can successfully find the maximum value in binary tree"
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(2)
    bst.add(1)
    bst.add(6)
    bst.add(7)
    bst.add(3)
    bst.add(4)
    bst.add(8)  
    bst.add(9)
    bst.add(10)
    expected = 10
    actual = bst.find_maximum_value()
    assert expected == actual

def test_11():
    bst=BinarySearchTree()
    bst.add(5)
    bst.add(90)
    bst.add(55)
    bst.add(25)
    bst.add(63)
    expected = 90
    actual = bst.find_maximum_value()
    assert expected == actual
"""
breadth first serch
"""
def test_12():
    bst=BinarySearchTree()
    bst.add(10)
    bst.add(40)
    bst.add(30)
    bst.add(25)
    bst.add(50)
    expected = [10, 40, 30, 50, 25]
    actual = bst.breadth_first(bst.root)
    assert expected == actual
"""
check if the breadth first tree is empty 
"""
def test_13():
    bst=BinarySearchTree()
    expected="Tree is empty"
    actual = bst.breadth_first(bst.root)
    assert expected == actual

    