class Solution:

  
  # fourth time? getting rusty 
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        first = dummy
        second = dummy
        ind = 0
        while ind < n and first:
            ind +=1
            first = first.next
        
        while first.next:
            first = first.next
            second = second.next
        
        if second == dummy:
            return head.next
        
        second.next = second.next.next
        return head
  
  
  
  
  
   # second time, approved solution
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
        
        dummy = ListNode(-1)
        dummy.next = head
        
        front = head
        ind = 1
        while ind < n:
            front = front.next
            ind += 1
        
        back = dummy
        while front and front.next:
            front = front.next
            back = back.next
       
            
        back.next = back.next.next
        
        return dummy.next






   #
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
            
        cur = head
        endInd = 1
        while cur and cur.next:
            endInd += 2
            cur = cur.next.next
            
        if cur is None:
            endInd -= 1
        
        # Edge Case
        if endInd - n == 0:
            head = head.next
            return head
        
        deleterInd = 1
        cur = head
        while True:
            if deleterInd == (endInd - n):
                if cur.next.next:
                    cur.next = cur.next.next
                else:
                    cur.next = None
                return head
            deleterInd += 1
            cur = cur.next