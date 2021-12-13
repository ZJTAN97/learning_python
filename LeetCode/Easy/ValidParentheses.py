def check_parentheses(s):

    if(len(s) % 2 != 0):
        return False

    stack = []

    for i in s:
        if(i == '('): 
            stack.append(')')
        elif (i == '{'):
            stack.append('}')
        elif (i == '['):
            stack.append(']')
        elif(len(stack) == 0 or stack.pop() != i):
            return False
    
    return len(stack) == 0


s = '{[]}'
print(check_parentheses(s))