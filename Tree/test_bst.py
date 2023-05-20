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

def test_6():
    "Can successfully add child left and right"
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(2)
    bst.add(6)
    expected =[2, 6, 5]
    actual = bst.traverse_postorder(bst.root)
    assert expected == actual