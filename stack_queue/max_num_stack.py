# how to get max number in stack?
from stack_queue.Stack import Stack
def find_max_element(stack):
    stack1 = Stack()
    max_num = 0
    for x in stack:
        if x > max_num:
            max_num = x
            stack1.push(x)
    if stack1.isEmpty():
            return "stack is empty"
    return max_num

arr=[1568,8633599,7941256525]
print(find_max_element(arr))