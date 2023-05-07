from stack_queue.Node import Node
class Queue():    
    def __init__(self):  
        self.head = None        
        self.tail = None
    """
    this function to check if the queue is empty or not and return true or false
    """
    def isEmpty(self):
        return self.head == None
    """
    to get the first element in the queue
    """
    def peek(self):
        if self.head:
            return self.head.value
        else:
            raise IndexError("Error : Empty Queue!")
    """
    this function work to add the value to the queue after check if its empty or not 
    """
    def enqueue(self, value):
        new_data = Node(value)
        if self.head is None:
           self.head = new_data
           self.tail = self.head
        else:
           self.tail.next = new_data
           self.tail = new_data
    """
    this function to delete element from the queue
    """
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Error : Empty Queue!")
        data = self.head.value
        self.head = self.head.next
        if self.head is None:
           self.tail is None
        return data
    """
    to print the queue 
    """
    def __str__(self):

        output = ""
        
        if self.head is None:
            output = "Empty queue"
        
        else:
            current = self.head
            while(current):
                output += f'{current.value} --> '
                current = current.next
            
            output += " None"
        return output