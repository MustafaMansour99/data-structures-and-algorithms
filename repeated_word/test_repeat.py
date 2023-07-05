import pytest
from repeated_word.repeated_word import repeated_word

def test_repeated_word1():
    # Test case 1
    word = "hi mustafa how are you hi mustafa"
    expected = "hi"
    assert repeated_word(word) == expected

def test_repeated_word2():
    # Test case 1
    word = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way - in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    expected = "it"
    assert repeated_word(word) == expected

def test_repeated_word3():
    # Test case 1
    word = "hi mustafa how are you"
    expected = "No Repetition"
    assert repeated_word(word) == expected