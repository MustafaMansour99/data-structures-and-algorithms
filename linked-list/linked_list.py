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
    """ 
    add three function to add node in the end of linked list (append)
    add a new_node befor target node (insert_before)
    add a new node after target node(insert_after)
    
    """
    def append(self, new_data):
 
        new_node = Node(new_data)
 
        
        if self.head is None:
            self.head = new_node
            return
 
        last = self.head
        while (last.next):
            last = last.next
 
        last.next =  new_node 
    def insert_before(self,target,value):
            node = Node(value)
            if self.head == None:
              self.insert(value)
            if self.head.value == target:
              self.insert(value)
            else:
              currnet = self.head
              while currnet.next.value is not target:
                   currnet = currnet.next
              target = currnet 
              node.next = target.next
              target.next = node

    def insert_after(self,target,value):
            node = Node(value)
            if self.head == None:
              self.insert(value)

            else:
              currnet = self.head
              while currnet.value is not target:
                   currnet = currnet.next
              target = currnet 
              node.next = target.next
              target.next = node
        


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
