"""
Python list itself can perform stack operations
- append() is used to add element to the top of the stack
- pop() removes the element in LIFO order.
"""

stack = []
stack.append('a')
stack.append('b')
stack.pop() # dont take in any arguments!!
print(stack)


"""
Implementation of stack using singly linked list
"""

class ListNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Stack:
    # initialize a stack with dummy node
    def __init__(self) -> None:
        self.head = ListNode("head")
        self.size = 0
    
    # String representation of the stack
    def __str__(self) -> str:
        curr = self.head.next
        out = ""
        while curr:
            out += str(curr.value) + "->"
            curr = curr.next
        return out[:-2]

    # Get current size of stack
    def getSize(self):
        return self.size == 0

    # Check if stack is empty
    def isEmpty(self):
        return self.size == 0
    
    # Get the top item of the stack
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
    
    # Push a value into the stack
    def push(self, value):
        node = ListNode(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    # Remove value from stack and return
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack.")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 13):
        stack.push(i)
    print(stack)

    for _ in range(1, 6):
        remove = stack.pop()
        print(remove)

    print(stack)