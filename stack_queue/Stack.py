from stack_queue.Node import Node
class Stack:
    def __init__(self):
        self.top = None

    def push(self,value):
        node = Node(value)
        if self.top:
            node.next=self.top
        self.top=node

    def pop(self):
         if self.top is None:
            raise ValueError("Error : Empty Stack!")
         
         temp=self.top
         self.top=self.top.next
         return temp.value
    
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
    
    def peek(self):
        if self.top:
            return self.top.value
        else:
            raise ValueError("Error : Empty Stack!")
         
              

       
    def isEmpty(self):
        return self.top == None

