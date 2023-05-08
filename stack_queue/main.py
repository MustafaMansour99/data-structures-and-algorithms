from stack_queue.Queue import Queue
from stack_queue.Stack import Stack
from stack_queue.Pseudo_Queue import pseudo_queue

q = pseudo_queue()
q.enQueue(1) 
q.enQueue(2) 
q.enQueue(3)
print(q.deQueue()) 
print(q)
# print(q.deQueue())
# print(q.deQueue())
# print(q.deQueue())
# print(q.deQueue())
# queue1 = Queue()

# queue1.enqueue(1)
# queue1.enqueue(2)
# queue1.enqueue(3)
# print(queue1.peek())
# print(queue1)
# # try:
# print(queue1.dequeue())
# print(queue1.dequeue())
# print(queue1.dequeue())
# print(queue1.peek())
# try:
#     print(queue1)
#     print(queue1.dequeue())
#     print(queue1.isEmpty())
# except IndexError as err:
#     print(err)    

# stack1 = Stack()
# stack1.push("A")
# stack1.push("B")
# stack1.push("C")
# print(stack1)
# try:
#     print(stack1.pop())
#     print(stack1)
#     # print(stack1.pop())
#     # print(stack1.pop())
#     # print(stack1.pop())
# except ValueError as err:
#     print(err)

# print(stack1.isEmpty())
