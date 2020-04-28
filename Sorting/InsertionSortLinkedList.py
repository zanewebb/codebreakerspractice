# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:


   # first try, i think its close, temp save 
    def insertionSortList(self, head: ListNode) -> ListNode:
        # should be O(N^2) solution
        
        if not head.next:
            return head
        
        # track current index with a counter, and track the current list node (starting on node 2)
        outerCounter = 1
        curNode = head.next
        
        # while currentNode
        while curNode:
            # hold onto currentNode's next
            outerNext = curNode.next
            
            # declare new subCurrent node iterator and count index and prev pointer
            subCurNode = head
            subCounter = 0
            prev = head
            
            # while the counter is less than the outer counter and subcurrentnode.val is < currentNode.val
            while subCounter < outerCounter and subCurNode.val < curNode.val:
                # prev = subcurrentNode
                prev = subCurNode
                # subcurrentnode = subcurrentNode.next
                subCurNode = subCurNode.next
                # counter += 1
                subCounter += 1
            
            # now that our prev pointer should be pointing at the node less than or equal to subcurrentnode
            # we can assign prev.next to our outer current node
            
            # EDGE CASE SOMEWHERE IN HERE CONCERNING THE HEAD POINTER
            # may not be needed?
            # if head == prev:
            #     head.next = curNode
            
            prev.next = curNode
            
            # and assign current node's next to what subCurrentNode ended up as
            curNode.next = subCurNode
            
            # assign current node to the saved next
            curNode = outerNext
        
        return head