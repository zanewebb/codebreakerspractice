# third time

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        newNodes = {}
        
        newHead = Node(-1)
        newCur = newHead
        cur = head
        ind = 0
        
        while cur:
            newCur.next = Node(cur.val)
            cur.val = str(cur.val) + str(ind)
            
            newNodes[cur.val] = newCur.next
            
            cur = cur.next
            newCur = newCur.next
            ind += 1
        
        cur = head
        newCur = newHead.next
        while cur:
            if cur.random:
                newCur.random = newNodes[cur.random.val]
            cur = cur.next
            newCur = newCur.next
        
        return newHead.next


# second time, had a lot of trouble, unsure how i crafted that solution next time, i need sleep 

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # should be two passes, one to duplicate and track randoms, 
        # one to assign randoms on copy
        
        # should be a dict of composite key (node val + index) : newNodes
        rands = {}
        
        ind = 0
        # start with dummy nodes
        cur = Node(-1, head, None)
        newCur = Node(-1, None, None)
        newHead = None
        while cur:
            if cur.next:
                temp = Node(cur.next.val)
                cur.next.val = str(temp.val) + str(ind)
                newCur.next = temp
                rands[cur.next.val] = temp
                
                if cur.next == head:
                    newHead = temp
            else:
                newCur.next = None
            
            ind += 1
            newCur = newCur.next
            cur = cur.next
        
        # assign rands
        cur = head
        newCur = newHead
        ind = 0
        while newCur:
            if cur.random:
                newCur.random = rands.get(cur.random.val, None)
            else:
                newCur.random = None
            cur = cur.next
            newCur = newCur.next
            ind += 1
        return newHead



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