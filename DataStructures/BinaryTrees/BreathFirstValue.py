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

def breath_first_values(root):
    if root is None:
        return []
    
    result = []
    queue = [root]

    while(len(queue) > 0):

        current = queue.pop(0)
        result.append(current.val)

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    
    return result


print(breath_first_values(a))