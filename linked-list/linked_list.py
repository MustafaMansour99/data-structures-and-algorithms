from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert (self,value):
           node = Node(value) 
           if self.head == None:
                self.head = node
           else:
                node.next = self.head
                self.head = node
    
    def includes(self, value):
        current = self.head
        if current is None:
             return False
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False
    
    def __str__(self):
        output = ""
        if self.head is None:
            output = "Empty LinkeList"
        else:
            current = self.head
            while(current):
                output += f'{current.value} --> '
                current = current.next
            
            output += " None"
        return output
