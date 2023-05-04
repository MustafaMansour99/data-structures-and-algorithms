from stack_queue.Node import Node
class Queue():    
    def __init__(self):  
        self.head = None        
        self.tail = None

    def isEmpty(self):
        return self.head == None
    
    def peek(self):
        if self.head:
            return self.head.value
        else:
            raise IndexError("Error : Empty Queue!")
    
    def enqueue(self, value):
        new_data = Node(value)
        if self.head is None:
           self.head = new_data
           self.tail = self.head
        else:
           self.tail.next = new_data
           self.tail = new_data
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Error : Empty Queue!")
        data = self.head.value
        self.head = self.head.next
        if self.head is None:
           self.tail is None
        return data
    
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