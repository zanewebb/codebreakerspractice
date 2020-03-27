# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            return None
        
        # make slow and fast iterators with associated length counters
        slow = fast = head
        slowPos = fastPos = 1
        
        # iterate with fast moving twice as fast as slow, 
        # counting how far into the list you are as you go
        snipped = False
        target = -1
        while True:
            # when fast hits the end, note the number, 
            if fast is None and target is -1:
                # subtract n from it and make that the target number
                target = fastPos - (n-1)
            
            # when the slow iterator gets to the target, snip that node from the linked list
            if target == 1:
                    head = head.next
                    break
            if slowPos+1 == target:
                # set the next pointer to the next next unless its the end of the list then
                # just remove the last node
                slow.next = slow.next.next if slow.next else None
                break
            if target is not -1:
                slow = slow.next
                slowPos += 1
            
            if fast:
                if fast.next:
                    if fast.next.next:
                        fast = fast.next.next
                        fastPos += 2
                    else:
                        fast = fast.next
                        fastPos += 1
                else:
                    fast = None
        
        
        
        #return head        
        return head
