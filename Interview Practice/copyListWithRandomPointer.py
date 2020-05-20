"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# first try, took a while but i got it
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        # store dict of known nodes val: node
        nodes = {}
        
        # iterate over the list once copying each one and tracking the nodes in the dict
        cur = Node(-1, head, None)
        newCur = Node(-1, None, None) 
        newHead = None
        count = 0
        while cur:
            # if there IS a next node
            if cur.next:
                # create a copy of that node
                newNode = Node(cur.next.val, None, None)
                cur.next.val = str(cur.next.val) + str(count)
                # assign it as the new list's cur's next
                newCur.next = newNode
                # make sure that we track it
                nodes[cur.next.val] = newNode
                # iterate down copy list
                newCur = newCur.next
                # set the head of the new list if applicable
                if cur.next == head:
                    newHead = newNode
            else:
                newCur.next = None
            # continue iterating
            cur = cur.next
            count += 1
        
        # n,N = head, newHead
        # print("old")
        # while n:
        #     print(n.val)
        #     n = n.next
        # print("New")
        # while N:
        #     print(N.val)
        #     N = N.next
        # print(nodes)
        
        
        # iterate a second time setting all of the random pointers using the dict
        cur = head
        newCur = newHead
        while cur:
            if cur.random:
                newCur.random = nodes[cur.random.val]
            else:
                newCur.random = None
            
            cur = cur.next
            newCur = newCur.next
            
            
        # n,N = head, newHead
        # print("old")
        # while n:
        #     print(n.val, n,  n.random.val if n.random else None)
        #     n = n.next
        # print("New")
        # while N:
        #     print(N.val, N, N.random.val if N.random else None)
        #     N = N.next    
        
        return newHead