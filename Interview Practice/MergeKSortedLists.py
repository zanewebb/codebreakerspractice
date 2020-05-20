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