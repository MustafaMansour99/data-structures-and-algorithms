import pytest
from Left_Join.left_join import left_join
def test1():
    hashmap1 = {
    'happy': 'joyful',
    'sad': 'unhappy',
    'big': 'large',
    'small': 'tiny'
}

    hashmap2 = {
    'happy': 'sad',
    'big': 'small',
    'small': 'big',
    'fast': 'slow'
}
    expectedOutput= {('big', 'large', 'small'), ('small', 'tiny', 'big'), ('happy', 'joyful', 'sad'), ('sad', 'unhappy', None)}
    
    assert(left_join(hashmap1,hashmap2) == expectedOutput)