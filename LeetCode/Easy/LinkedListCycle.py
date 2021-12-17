class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head):

        if head == None: return False

        slow = head
        fast = head.next

        while(fast != None and fast.next != None):

            slow = slow.next
            fast = fast.next.next

            if slow == fast: return True
        
        return False

            

solution = Solution()

first = ListNode(3)
second = ListNode(2)
third = ListNode(0)
fourth = ListNode(-4)

first.next = second
second.next = third
third.next = fourth
fourth.next = second

print(solution.hasCycle(first))