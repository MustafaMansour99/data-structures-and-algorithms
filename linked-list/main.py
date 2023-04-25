from linked_list import LinkedList

if __name__ == "__main__":

    linked_list1 = LinkedList()

    linked_list1.insert("A")
    linked_list1.insert("B")
    linked_list1.insert("C")
    linked_list1.append("f")
    linked_list1.append("g")
    linked_list1.insert_after("A","M")
    print(linked_list1.kth_from_end(-8))

    
    print(linked_list1)

    print(linked_list1.includes("A"))
