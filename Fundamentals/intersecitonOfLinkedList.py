# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        
        
        # iterate across head A and B to see if the final node is the same for both
        curA = headA
        curB = headB
        prevA = prevB = None
        while curA:
            prevA = curA
            curA = curA.next
        while curB:
            prevB = curB
            curB = curB.next
            
        # if the final node is the same for both heads' iterators, there was an intersection
        # else return null
        if prevA != prevB:
            return None
        
        # Since there was an intersection, iterate over both of them over and over until they are the same node
        # either they are the same length prior to intersection and will collide on the first pass
        # or they will be offset and eventually collide
        curA = headA
        curB = headB
        intersectNode = None
        
        while intersectNode is None:
            if curA is None:
                curA = headB
            if curB is None:
                curB = headA
                
            #print("checking A: "+str(curA.val) + " and  B: "+ str(curB.val))
            if curA == curB:
                intersectNode = curA
            curA = curA.next
            curB = curB.next
        return intersectNode




# third time

def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        
        curA = headA
        curB = headB
        while curA.next:
            curA = curA.next
        while curB.next:
            curB = curB.next
            
        if curA != curB:
            return None
        
        curA = headA
        curB = headB
        while curA != curB:
            curB = curB.next
            curA = curA.next
            if not curA:
                curA = headB
            if not curB:
                curB = headA
            
            
            
        return curA


#Second time

class Solution:
   
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        
        a = headA
        b = headB
        
        while a.next:
            a = a.next
        while b.next:
            b = b.next
        
        if a != b:
            return None
        
        a = headA
        b = headB
        while True:
            if not a:
                a = headB
            if not b: 
                b = headA
            if a == b:
                return a
            a = a.next
            b = b.next
        

# 4,1,8,4,5,4,1,8,4,5,4,1,8,4,5,4,1,8,4,5,4,1,8,4,5,4,1,8|,4,5,4,1,8,4,5,4,1,8,4,5,4,1,8,4,5,4,1,8,4,5
# 5,0,1,8,4,5,5,0,1,8,4,5,5,0,1,8,4,5,5,0,1,8,4,5,5,0,1,8|,4,5,5,0,1,8,4,5,5,0,1,8,4,5,5,0,1,8,4,5,
#


 # run through the linked lists once, counting length and storing "prev"
      #   lenA = lenB = 0
      #   curA = headA
      #   curB = headB
      #   prevA = prevB = None
      #   while curA:
      #       lenA += 1
      #       prevA = curA
      #       curA = curA.next
      #   while curB:
      #       lenB += 1
      #       prevB = curB
      #       curB = curB.next
      #   # if the final node is the same for both heads' iterators, there was an intersection
      #   # else return null
      #   if prevA != prevB:
      #       return None
        
      #   # pick the shorter head and iterate over it for headLength - the difference between the two headlengths 
      #   diff = abs(lenA - lenB)
      #   if diff == 0:
      #       return prevA
        
      #   curA = headA
      #   curB = headB
      #   if lenA < lenB:
      #       for i in range(0, lenA-diff):
      #           curA = curA.next
