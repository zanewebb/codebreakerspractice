# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# second time
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c1, c2, nh = l1, l2, ListNode(-1)
        cur = nh
        remainder = 0
        while c1 or c2:
            num = 0
            if not c1:
                num = c2.val + remainder
                c2 = c2.next
            elif not c2:
                num = c1.val + remainder
                c1 = c1.next
            else:
                num = c1.val + c2.val + remainder
                c1 = c1.next
                c2 = c2.next
                
            # 12 // 10 = 1
            # 
            remainder = num // 10
            
            # 12 % 10 = 2
            ones = num % 10
            
            cur.next = ListNode(ones)
            cur = cur.next
            
        if remainder:
            cur.next = ListNode(remainder)
            
        return nh.next

# first time

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        c1, c2 = l1, l2
        nh = ListNode(-1)
        nc = nh
        remainder = 0
        while c1 or c2:
            if c1 and c2:
                newval = c1.val + c2.val + remainder
                c1 = c1.next
                c2 = c2.next
            elif c1 and not c2:
                newval = c1.val + remainder
                c1 = c1.next
            elif c2 and not c1:
                newval = c2.val + remainder
                c2 = c2.next
            
            remainder = 0
            
            if newval >= 10:
                remainder = (newval - (newval % 10)) // 10
                newval = newval % 10
                
            nc.next = ListNode(newval)
            nc = nc.next
            
        if remainder != 0:
            nc.next = ListNode(remainder)
            nc = nc.next
        
        return nh.next