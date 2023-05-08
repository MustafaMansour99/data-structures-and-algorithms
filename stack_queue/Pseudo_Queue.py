class pseudo_queue: 
    """
    this class Implement a Queue using two Stacks
    """
    def __init__(self):
        """
        declare tow stack as list
        """
        self.s1 = []
        self.s2 = []
  
    def enQueue(self, x):
        """
        this function to add element to stack 2 from stack 1
        """
        # Move all elements from s1 to s2 
        while len(self.s1) != 0: 
            self.s2.append(self.s1[-1]) 
            self.s1.pop()
  
        # Push item into self.s1 
        self.s1.append(x) 
  
        # Push everything back to s1 
        while len(self.s2) != 0: 
            self.s1.append(self.s2[-1]) 
            self.s2.pop()
  
    # Dequeue an item from the queue 
    def deQueue(self):
          
            # if first stack is empty 
        if len(self.s1) == 0: 
            print("Q is Empty")
      
        # Return top of self.s1 
        x = self.s1[-1] 
        self.s1.pop() 
        return x

    def __str__(self):
        return str(self.s1)
    
