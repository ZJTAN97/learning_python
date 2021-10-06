"""
GeeksForGeeks way of implementing
"""
class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self) -> None:
        self.head = None

    
    def show_list(self) -> None:
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next



"""
LeetCode + my way of implementing
"""
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    
    def show_list(self):
        while(self):
            print(self.data)
            self = self.next



if __name__ == '__main__':

    sample = LinkedList()
    sample.head = Node(1)
    second = Node(2)
    third = Node(3)

    sample.head.next = second
    second.next = third

    sample.show_list()


    sample2 = ListNode(0)
    sample2_next = ListNode(1)
    sample2.next = sample2_next
    sample2.show_list()


    