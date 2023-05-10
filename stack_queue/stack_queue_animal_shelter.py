from stack_queue.Queue import Queue
class AnimalShalter:
    """
    This code defines an AnimalShelter class that has two queues, one for cats and one for dogs. 
    """
    def __init__(self):
        self.cats = Queue()
        self.dog =Queue()
    """
    this function that takes an object representing an animal as input and enqueues it into the corresponding queue based on its species (either "cat" or "dog").
    """
    def enqueue(self,obj):
        if obj["species"] == "cat":
            self.cats.enqueue(obj)
        if obj["species"] == "dog":
            self.dog.enqueue(obj)
    """
    The dequeue function takes a string representing the animal's species ("cat" or "dog") as input and dequeues the animal at the front of the corresponding queue
    """

    def dequeue(self,animal):
        if animal== "cat":
            return self.cats.dequeue()
        if animal == "dog":
            return self.dog.dequeue()
        else:
            return "null"