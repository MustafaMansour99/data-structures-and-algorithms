import pytest
from stack_queue.Queue import Queue
from stack_queue.Stack import Stack
"""
Test file for queue and stack
"""
def test_1():
    queue = Queue()
    expected = "Empty queue"
    actual = str(queue)
    assert expected == actual

def test_2(queue):
    expected="1 --> 2 --> 3 -->  None"
    actual = str(queue)
    assert expected == actual
def test_3(queue):
    queue.dequeue()
    expected = "2 --> 3 -->  None"
    actual = str(queue)
    assert expected == actual
def test_4(queue):
    queue.dequeue()
    queue.dequeue()
    expected = "3 -->  None"
    actual = str(queue)
    assert expected == actual
def test_5(queue):
   expected = ("1")
   actual = queue.peek()
   assert expected == actual
def test_55(queue):
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    assert queue.isEmpty() == True

def test_6(queue):
   with pytest.raises(IndexError):
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.peek()

def test_7():
    stack = Stack()
    expected = "stack empty!"
    actual = str(stack)
    assert expected == actual

def test_8(stack):
    expected='C --> B --> A -->  None'
    actual = str(stack)
    assert expected == actual

def test_9(stack):
    stack.pop()
    expected = "B --> A -->  None"
    actual = str(stack)
    assert expected == actual
def test_10(stack):
    stack.pop()
    stack.pop()
    stack.pop()
    expected = "stack empty!"
    actual = str(stack)
    assert expected == actual

def test_11(stack):
   expected = ("C")
   actual = stack.peek()
   assert expected == actual


def test_12(stack):
    with pytest.raises(ValueError):
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.peek()


@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue("1")
    queue.enqueue("2")
    queue.enqueue("3")
    
    return queue

@pytest.fixture
def stack():
    stack = Stack()
    stack.push("A")
    stack.push("B")
    stack.push("C")
    
    return stack