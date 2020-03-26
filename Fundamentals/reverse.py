from LinkedList import LinkedList

def reverse(linkedlist):
   cur = linkedlist.head.next
   prev = None

   while cur is not None:
      next = cur.next
      cur.next = prev
      prev = cur
      cur = next
   linkedlist.head.next = prev

   return linkedlist



if __name__ == "__main__":
   linkedlist = LinkedList()
   for i in range(1,6):
      linkedlist.insertFront(i)
   print(linkedlist)

   print(reverse(linkedlist))