import pytest
from repeated_word.repeated_word import repeated_word

def test_repeated_word1():
    # Test case 1
    word = "hi mustafa how are you hi mustafa"
    expected = "hi"
    assert repeated_word(word) == expected

def test_repeated_word2():
    # Test case 1
    word = "hi mustafa how are you"
    expected = "No Repetition"
    assert repeated_word(word) == expected