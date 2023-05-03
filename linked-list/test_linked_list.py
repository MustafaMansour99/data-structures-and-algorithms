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

def test_7(ll):
    expected ="C --> B --> A --> f -->  None"
    ll.append("f")
    actual = str(ll)
    assert expected == actual
def test_8(ll):
    expected ="C --> B --> A --> f --> g -->  None"
    ll.append("f")
    ll.append("g")
    actual = str(ll)
    assert expected == actual

def test_9(ll):
    expected = "M --> C --> B --> A -->  None"
    ll.insert_before("C","M")
    actual = str(ll)
    assert expected == actual
def test_10(ll):
    expected = "C --> B --> M --> A -->  None"
    ll.insert_before("A","M")
    actual = str(ll)
    assert expected == actual

def test_11(ll):
    expected = "C --> B --> M --> A -->  None"
    ll.insert_after("B","M")
    actual = str(ll)
    assert expected == actual
def test_11(ll):
    expected = "C --> B --> A --> M -->  None"
    ll.insert_after("A","M")
    actual = str(ll)
    assert expected == actual
def test_12(ll):
    expected = "the K is greater than linked list or not positive number"
    actual = ll.kth_from_end(8)
    assert expected == actual
def test_13(ll):
    expected = "B"
    actual = ll.kth_from_end(2)
    assert expected == actual
def test_14(ll):
    expected = "the K is greater than linked list or not positive number"
    actual = ll.kth_from_end(-5)
    assert expected == actual
def test_14(ll):
    expected = "A"
    actual = ll.kth_from_end(1)
    assert expected == actual

def test_15():
    ll=LinkedList()
    ll.append("a")
    ll.append("b")
    ll.append("c") 
    ll2=LinkedList()
    ll2.append("1")
    ll2.append("2")
    ll2.append("3") 
    excepted="a --> 1 --> b --> 2 --> c --> 3 -->  None"
    actual=str(ll.zip_list(ll,ll2))
    assert actual == excepted 

def test_18():
    ll=LinkedList()
    ll.append("a")
    ll.append("b")
    ll2=LinkedList()
    ll2.append("1")
    ll2.append("2")
    ll2.append("3") 
    excepted="a --> 1 --> b --> 2 --> 3 -->  None"
    actual= str(ll.zip_list(ll,ll2))
    assert actual == excepted   

def test_19():
    ll=LinkedList()
    ll.append("a")
    ll.append("b")
    ll.append("c") 
    ll2=LinkedList()
    ll2.append("1")
    ll2.append("2")
    excepted="a --> 1 --> b --> 2 --> c -->  None"
    actual=str(ll.zip_list(ll,ll2))
    assert actual == excepted 

def test_20():
    ll=LinkedList()
    ll.append("a")
    ll.append("b")
    ll.append("c") 
    ll2=LinkedList()
    excepted="a --> b --> c -->  None"
    actual=str(ll.zip_list(ll,ll2))
    assert actual == excepted

def test_20():
    ll=LinkedList() 
    ll2=LinkedList()
    ll2.append("1")
    ll2.append("2")
    excepted="1 --> 2 -->  None"
    actual=str(ll.zip_list(ll,ll2))
    assert actual == excepted

def test_22():
    ll=LinkedList() 
    ll2=LinkedList()
    excepted="Both Linkedlists are empty"
    actual=str(ll.zip_list(ll,ll2))
    assert actual == excepted

@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert("A")
    ll.insert("B")
    ll.insert("C")
    
    return ll