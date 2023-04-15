import pytest
from linked_list import LinkedList

def test_empty_ll():
    ll = LinkedList()
    expected = "Empty LinkeList"
    actual = str(ll)
    assert expected == actual

def test_two(ll):
    expected = "C --> B --> A -->  None"
    actual = str(ll)
    assert expected == actual

def test_three(ll):
    expected = "C"
    actual = ll.head.value
    assert expected == actual

def test_Four(ll):
    expected = "C --> B --> A -->  None"
    actual = str(ll)
    assert expected == actual

    '''
    Can properly insert multiple nodes into the linked list??
    yes
    '''
def test_five(ll):
    expected= True
    actual = ll.includes("C")
    assert expected == actual

def test_six(ll):
    expected =False
    actual = ll.includes("F")
    assert expected == actual

@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert("A")
    ll.insert("B")
    ll.insert("C")
    
    return ll