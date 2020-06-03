# third time?

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        
        # heap that will store (node value, list index)
        listnodes = {}
        heap = []
        for i, l in enumerate(lists):
            listnodes[i] = l
            if l:
                heap.append((l.val, i))
        
        heapq.heapify(heap)
        head = ListNode(-999)
        cur = head
        
        while len(heap) > 0:
            heapnode = heapq.heappop(heap)
            cur.next = listnodes[heapnode[1]]
            listnodes[heapnode[1]] = listnodes[heapnode[1]].next
            if listnodes[heapnode[1]]:
                heapq.heappush(heap, (listnodes[heapnode[1]].val, heapnode[1]))
            cur = cur.next    
        return head.next



# remembered it mostly, forgot the key detail that the tuple must store the index of the list and not the list node itself
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        newLists = []
        for i,l in enumerate(lists):
            if l:
                newLists.append((l.val, i))
        
        
        # print(newLists)
        heapq.heapify(newLists)
        
        finalList = ListNode(-1)
        cur = finalList
        
        while len(newLists) > 0:
            nextList = heapq.heappop(newLists)
            cur.next = lists[nextList[1]]
            lists[nextList[1]] = lists[nextList[1]].next
            
            if lists[nextList[1]]:
                heapq.heappush(newLists,(lists[nextList[1]].val, nextList[1]))
            cur = cur.next
            
        return finalList.next   




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# messy but the trick to using it in this case is to track the index of the list and alter it in place instead of moving it into the heap


import heapq

def mergeKLists(lists):
   pq = []
   
   head = cur = ListNode(-1)
   
   # add all lists to heap
   for ind, l in enumerate(lists):
      if l:
            pq.append((l.val,ind))
   # in-place conversion to a heap
   heapq.heapify(pq)
   print(pq)
   
   while pq:
      val, ind = heapq.heappop(pq)
      cur.next = ListNode(val)
      cur = cur.next
      lists[ind] = lists[ind].next
      if lists[ind]:
            heapq.heappush(pq, (lists[ind].val, ind))
   
   return head.next


class ListNode:
   def __init__(self, val):
      self.val = val
      self.next = None


if __name__ == "__main__":
   lists = []
   vals = [1,4,5,-1,1,3,4,-1,2,6,-1]

   head = cur = ListNode(-1)
   for v in vals:
      if v == -1:
         lists.append(head.next)
         head = cur = ListNode(-1)
      else:
         cur.next = ListNode(v)
         cur = cur.next
   
   head = mergeKLists(lists)

   while head:
      print(head.val)
      head = head.next