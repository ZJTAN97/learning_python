class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def depth_first_values(root):
    if root is None: 
        return []
    
    result = []
    stack = [root]

    while len(stack) > 0:
        current = stack.pop()
        result.append(current.val)

        if current.left is not None: 
            stack.append(current.left)
        if current.right is not None:
            stack.append(current.right)

    return result


def depth_first_values_recursive(root):

    if root is None: 
        return []
        
    left_values = depth_first_values_recursive(root.left)
    right_values = depth_first_values_recursive(root.right)

    return [root.val] + left_values + right_values
            

        
print(depth_first_values(a))
print(depth_first_values_recursive(a))