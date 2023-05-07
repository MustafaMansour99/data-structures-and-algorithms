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
    def kth_from_end(self,k):
         if self.head is None:
            return None
         current = self.head
         length = 0
         while current:
            length += 1
            current = current.next
         if k > length or k < 0:
             return "the K is greater than linked list or not positive number"
         

         pointer1 =self.head
         pointer2 = self.head

         for i in range(k):
             pointer2 = pointer2.next
         while pointer2 is not None:
             pointer1 = pointer1.next
             pointer2 = pointer2 .next
         return pointer1.value
    
    def zip_list (self,list1,list2):
        """this function takes two linked list and zip them togather """
        list1_head = list1.head                 
        list2_head = list2.head 
        if list1_head == None and list2_head == None: 
            return "Both Linkedlists are empty"               
        elif list1_head == None:
            return list2             
        elif list2_head == None:
            return list1
        else:
            current = list1.head
            current_2 =list2.head
            while current and current_2  :
                if current:
                    temp = current.next
                    current.next = current_2
                    current=temp

                if current_2:
                     temp_2 = current_2.next
                     current_2.next = temp
                     current_2 = temp_2


            if current_2:
                while current_2 :
                    list1.append(current_2.value)
                    current_2=current_2.next


        return list1
    def reverse_linked_list(self):
        """this function takes a linked list and reverses it"""
        current = self.head
        previous = None
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
            self.head = previous
        return self.head

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
