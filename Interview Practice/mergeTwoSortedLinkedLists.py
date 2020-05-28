# second time, sloppy execution, how am i doing worse than the first time i saw it???

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        c1, c2 = l1, l2
        
        if not c1:
            return c2
        if not c2:
            return c1
        
        # only advance the cur of a given list if we've chosen a val for it
        
        # decide the head
        nh = c1 if c1.val <= c2.val else c2
        n = ListNode(-1)
        # while c1 or c2
        while c1 or c2:
            if not c1:
                n.next = c2
                c2 = c2.next
                n = n.next
            elif not c2 :
                n.next = c1
                c1 = c1.next
                n = n.next
            elif c2.val < c1.val:
                n.next = c2
                c2 = c2.next
                n = n.next
            elif c1.val <= c2.val:
                n.next = c1
                c1 = c1.next
                n = n.next
        
        return nh

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if not l1 and l2:
            return l2
        if l1 and not l2:
            return l1
        
        # choose the inital head
        newHead = l1 if l1.val < l2.val else l2
        
        # set curs for each list and for the list we're making
        cur1, cur2, newCur = l1, l2, newHead
        if newHead == cur1:
            cur1 = cur1.next
        elif newHead == cur2:
            cur2 = cur2.next
            
        # iterate over the l1 and l2 lists adding to the newCur until both are None
        while cur1 or cur2:
            # other list is exhausted, fill out the rest of the new list
            if not cur1:
                newCur.next = cur2
                cur2 = cur2.next
            elif not cur2:
                newCur.next = cur1
                cur1 = cur1.next
            else:
                if cur1.val > cur2.val:
                    newCur.next = cur2
                    cur2 = cur2.next
                else:
                    newCur.next = cur1
                    cur1 = cur1.next
                
            newCur = newCur.next
        
        return newHead