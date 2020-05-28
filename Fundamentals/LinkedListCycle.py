#Linked List Cycle

# sixth time
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        
        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False

# fourth time??

def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        
        fast = slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast:
                return True
        
        return False


# third time, better solution improved

def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        
        fast = slow = head
        while fast and slow and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                return True
        
        return False


# garbage solution
# O(N) run time
# O(N) space
def hasCycle(self, head: ListNode) -> bool:
   # garbage solution
   # O(N) run time
   # O(N) space
   seen = []
   
   cur = head
   ind = 0
   while cur is not None:
      if cur in seen:
            return ind
      seen.append(cur)
      cur = cur.next
      ind += 1


   slow = fast = head
   ind = 0
   while slow is not None and fast is not None:
      if slow == fast:
         return
      ind += 1
      slow = slow.next
      fast = fast.next.next


   #less garbage solution 
   slow = fast = head
        ind = 0
        while slow is not None and fast is not None:
            if slow == fast and ind is not 0:
                return True
            ind += 1
            slow = slow.next
            fast = fast.next
            if fast is None: 
                break
            fast = fast.next
        
        return False


#second time around

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        
        slow = fast = head
        pos = 0
        while fast is not None and slow is not None:
            if fast == slow and pos != 0:
                return True
            slow = slow.next
            fast = fast.next.next if fast.next else None
            pos += 1
        
        return False
