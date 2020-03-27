#Linked List Cycle


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