from stack_queue.Node import Node
class Stack:
    def __init__(self):
        self.top = None
    """
    this function work to add the value to the Stack 
    """
    def push(self,value):
        node = Node(value)
        if self.top:
            node.next=self.top
        self.top=node
    """
    this function to delete element from the Stack
    """
    def pop(self):
         if self.top is None:
            raise ValueError("Error : Empty Stack!")
         
         temp=self.top
         self.top=self.top.next
         return temp.value
    """
    to print the Stack 
    """
    def __str__(self):

        output = ""
        
        if self.top is None:
            output = "stack empty!"
        else:
            current = self.top
            while(current):
                output += f'{current.value} --> '
                current = current.next
            
            output += " None"
        return output
    """
    to get the first element in the Stack
    """
    def peek(self):
        if self.top:
            return self.top.value
        else:
            raise ValueError("Error : Empty Stack!")
         
              

    """
    this function to check if the queue is empty or not and return true or false
    """
    def isEmpty(self):
        return self.top == None

