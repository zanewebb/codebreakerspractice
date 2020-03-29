class Solution:
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