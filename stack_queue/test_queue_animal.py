import pytest
from stack_queue.stack_queue_animal_shelter import AnimalShalter
 
def test_animal_cat(AA):
    assert AA.dequeue("cat") == {'species': 'cat', 'name': 'losy'}
def test_animal_dog(AA):
    assert AA.dequeue("dog") == {'species': 'dog', 'name': 'jack'}

@pytest.fixture
def AA():
    AA = AnimalShalter()
    AA.enqueue({"species":"cat","name":"losy"})
    AA.enqueue({"species":"dog","name":"jack"})
    AA.enqueue({"species":"cat","name":"kkk"})
    AA.enqueue({"species":"cat","name":"jjj"})

    return AA