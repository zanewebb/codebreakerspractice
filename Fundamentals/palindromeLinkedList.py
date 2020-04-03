# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    # 3rd time

    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next
        slow.next = None
        
        reversedList = self.reverse(mid)
        
        cur1 = head
        cur2 = reversedList
        while cur1 and cur2:
            if cur1.val != cur2.val :
                return False
            cur1 = cur1.next
            cur2 = cur2.next
        
        # if cur1 != cur2:
        #     return False
        
        return True
    
    def reverse(self, head: ListNode) -> ListNode:
        prev = temp = None
        cur = head
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev


# 2nd time aroun, coded properly this time

# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        # iterate at half and double speed
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # when fast hits the end, slow.next must bet the mid
        mid = slow.next
        slow.next = None #break the pointer
        
        # reverse the middle - end of the linkedlist
        endreversed = reverse(mid)
        
        # iterate from beginning and the middle(reversed), checking that the values match
        cur = endreversed
        slow = head
        while slow and cur:
            if slow.val != cur.val:
                return False
            slow = slow.next
            cur = cur.next
        return True
        
def reverse(head: ListNode) -> bool:
    
    prev = None
    cur = head
    temp = None
    
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev





#====================================================

        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        if head.next.next is None and head.next.val != head.val:
            return False
        
        # iterate at fast and sloe (2x and 1x) to find the midpoint.
        fast = head.next
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # using this midpoint pointer, reverse the remaining nodes
        mid = slow
        slow.next = None
        endReversed = reverse(mid)

        # reset the slow iterator to the beginning
        slow = head

        # iterate across both at 1x speed and evaluate if they have matching values
        while endReversed:
            if slow.val != endReversed.val:
                return False

        return True
    


# REVERSE IS BUILT WRONG
def reverse( head: ListNode) -> ListNode:
    
    temp = None
    prev = None
    
    
    while head is not None:
        temp = head.next # O prev  O head -> O temp
        head.next = prev # O prev <- O head  O temp
        prev = head      # O <- O prev/head  O temp
        head = temp      # O <- O prev  O temp/head
    return prev