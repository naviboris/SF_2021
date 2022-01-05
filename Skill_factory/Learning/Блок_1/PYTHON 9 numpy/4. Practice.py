from collections import deque

def brackets(line):
    stack = deque()
    
    for i in line:
        
        if line == "(":
            stack.append(line)
        elif line == ')':
            if len(stack) == 0:
                return False
            stack.pop()
        if len(stack) == 0:
            return True
    return False
            
