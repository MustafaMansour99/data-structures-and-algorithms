from stack_queue.stack_queue_brackets import validate_brackets
import pytest
def test_1():
    assert validate_brackets('{[()]}') == True
def test_2():
    assert validate_brackets('{[(') == False
def test_3():
    assert validate_brackets('')==True
def test_4():
    assert validate_brackets('mustafa mansour')==True
def test_5():
    assert validate_brackets('[mustafa mansour]')==True
def test_6():
    assert validate_brackets('{[mustafa mansour]}')==True