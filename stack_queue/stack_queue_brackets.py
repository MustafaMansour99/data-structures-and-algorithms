from stack_queue.Stack import Stack
def validate_brackets(string):
    """
    param string: string
    return: boolean
    """
    stack = Stack()
    # Loop for checking string
    for char in string:
        # if its opening bracket, so push it in the 
        # stack
        if char == '(' or char == '[' or char == '{':
            stack.push(char)
        # if its closing bracket, so pop it from the stack
        # if the top of the stack is the same as the   
        # closing bracket, then pop it
        elif char == ')' or char == ']' or char == '}':
            if stack.get_size()== 0:
                return False
            top_element = stack.pop()
            if (top_element == '(' and char != ')') or (top_element == '[' and char != ']') or (top_element == '{' and char != '}'):
                return False
            else:
                pass
        
    if stack.get_size()>0:
        return False
    return True
            


string = "{[]{()}}"
print(string,"-", validate_brackets(string))
 
string = "[[]"
print(string,"-", validate_brackets(string))
 