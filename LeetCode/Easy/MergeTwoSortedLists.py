class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_list(self):
        while self:
            print(self.val)
            self = self.next
        

class Solution:
    
    def mergeTwoLists(self, l1, l2):

        return_l = ListNode(0)
        current_l = return_l # think of it as a tail

        while l1 and l2:

            if l1.val < l2.val:
                current_l.next = l1
                l1 = l1.next
            else:
                current_l.next = l2
                l2 = l2.next
            
            current_l = current_l.next # have to update tail pointer
        
        if l1 != None:
            current_l.next = l1
            l1 = l1.next
        
        if l2 != None:
            current_l.next = l2
            l2 = l2.next
        
        return return_l.next # to remove the 0

        

if __name__ == '__main__':
    
    l1_head = ListNode(1)
    l1_second = ListNode(3)
    l1_third = ListNode(5)
    l1_head.next = l1_second
    l1_second.next = l1_third

    l2_head = ListNode(2)
    l2_second = ListNode(4)
    l2_third = ListNode(6)
    l2_head.next = l2_second
    l2_second.next = l2_third

    solution = Solution()
    solution.mergeTwoLists(l1_head, l2_head)




        