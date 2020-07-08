# seventh try, got it, forgot about keeping track of the keys in the nodes at first though
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.nodes = {}
        self.queue = None
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.nodes:
            # fetch value in that node
            ret = self.nodes[key].val
            
            # remove it from the queue
            self.remove(self.nodes[key])
            
            # re add it to the front
            newNode = Node(key, ret)
            self.addToFront(newNode)
            self.nodes[key] = newNode
            
            return ret
            
        else:
            return -1

        
    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.remove(self.nodes[key])
            newNode = Node(key, value)
            self.nodes[key] = newNode
            self.addToFront(newNode)
        else:
            newNode = Node(key, value)
            self.nodes[key] = newNode
            self.addToFront(newNode)
            self.size += 1
            
            # remove the least used if we exceed capacity
            if self.size > self.cap:
                delkey = self.remove(self.tail)
                self.nodes.pop(delkey, None)
                self.size -= 1
        
    def remove(self, node):
        # case where node is the only node in the list
        if node.prev is None and node.next is None:
            self.head = self.tail = None
            
        # case where we remove the tail and there are other elements
        elif node.next is None:
            node.prev.next = None
            self.tail = node.prev
        # case where wer remove the head and there are other elements
        elif node.prev is None:
            node.next.prev = None
            self.head = node.next
        # standard case, removing node somewhere in the middle of the queue
        elif node.prev is not None and node.next is not None:
            node.next.prev = node.prev
            node.prev.next = node.next        
            
        return node.key
        
    def addToFront(self, node):
        if self.head is not None:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        
        
        
class Node:
    def __init__(self, key=None, val=None):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# sixth try, got it after waaaay too long debugging, single class seems to reduce bugs in my setup, there are less edge cases than i think for the removal of a node

class ListNode:
    def __init__(self, key, val):
        self.next = None
        self.key = key
        self.val = val
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.nodes = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        # print("Before Get:")
        # self.printList()
        # print(self.nodes.keys())
        ret = -1
        if key in self.nodes:
            # track return value
            ret = self.nodes[key].val
            
            # refresh the node
            refr = self.nodes[key]
            self.removeNode(refr)
            self.placeFront(refr)
            # print("After Successful Get:")
            # self.printList()
            return ret
        return ret

    def put(self, key: int, value: int) -> None:
        #repl = True if key in self.nodes else False
        
        if key in self.nodes:
            self.removeNode(self.nodes[key])
        
        self.nodes[key] = ListNode(key, value)
        self.placeFront(self.nodes[key])
        
        print(len(self.nodes),self.cap)
        if len(self.nodes) > self.cap:
            # print("tail is", self.tail.key, self.tail.val )
            remKey = self.removeNode(self.tail)
            self.nodes.pop(remKey)
            # print("after removal",len(self.nodes),self.cap)
            # print(self.nodes.keys())
    
    def removeNode(self, delNode):
            if delNode.prev and delNode.next:
                delNode.prev.next = delNode.next
                delNode.next.prev = delNode.prev
            elif delNode == self.head and delNode.next:
                delNode.next.prev = None
                self.head = delNode.next
            elif delNode == self.tail and delNode.prev:
                delNode.prev.next = None
                self.tail = delNode.prev
            # this else case means that there is only one node in the list
            else:
                self.head = None
                self.prev = None
            
            # self.printList()
            
            delNode.next = None
            delNode.prev = None
            return delNode.key

    def placeFront(self, refr):
        refr.prev = None
        refr.next = self.head
        self.head = refr
        
        if refr.next == None:
            self.tail = refr
        else:
            refr.next.prev = self.head
            
    def printList(self):
        cur = self.head
        string = ""
        while cur:
            string += "-> ("+str(cur.key)+","+str(cur.val)+") "
            cur = cur.next
        print(string)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# fifth try

    # I dont understand why I cant get this one right. "wrong answer" on test case 14
    # not sure what about this test case maakes it crippling
    # ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
    # [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    def __str__(self):
        return "(" + str(self.key)+","+str(self.val)+")"
    def __repr__(self):
        return "(" + str(self.key)+","+str(self.val)+")"
        
class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # function for adding to front
    def add(self, node: Node):
        # using node, assign node's next to be head
        node.next = self.head
        # assign self.head's prev to be node
        if self.head:
            self.head.prev = node
        else:
            self.tail = node
        # assign self.head to be node
        self.head = node
    
    # function for removing from back
    def removeFromBack(self) -> int:
        #print( self.tail)
        # capture the key from the self.tail node
        retKey = self.tail.key
        if self.tail.prev:
            self.tail.prev.next = None
            # set self.tail equal to self.tail.prev
            self.tail = self.tail.prev
        
        # otherwise, set self.head and self.tail to None
        else:
            self.head = self.tail = None
        
        return retKey
        
    # function for refreshing a key in the Deque
    def refreshNode(self, node: Node):
        # if the node has a prev and a next
        if node.prev and node.next:
            # set node.prev.next to node.next
            node.prev.next = node.next
            # set node.next.prev to node.prev
            node.next.prev = node.prev
            self.add(node)
        # if node has no next, node must be tail
        elif not node.next:
            # remove from back
            self.removeFromBack()
            # add to front
            self.add(node)
            
        # if node has no prev, node must be head, do nothing
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.values = {}
        self.deque = Deque()

    def get(self, key: int) -> int:
        #print("get")
        # get node from self.values
        if key not in self.values:
            return -1
        else:
            node = self.values[key]
            # refresh node in deque by passing the node
            self.deque.refreshNode(node)
            # return the node.val
            return node.val

    def put(self, key: int, value: int) -> None:
        # if the key is already in the dict
        if key in self.values:
            # using that node, update the value 
            node = self.values[key]
            node.val = value
            # refresh that node
            self.deque.refreshNode(node)
        # otherwise
        else:
            # create a node
            node = Node(key, value)
            # add it to the dict
            self.values[key] = node
            # add it to the deque
            self.deque.add(node)
            # increment our size
            self.size += 1
            # check if the size is greater than the capacity
            if self.size > self.capacity:
                # if so, remove from the back of the deque and capture the popped key
                retKey = self.deque.removeFromBack()
                # remove that entry from the values dict
                self.values.pop(retKey, None)
                # decrement the size
                self.size -= 1
        #print(len(self.values.values()))
        print(self.values)
            

# fourth try, somehow hit an edge case with a key error after like 80 transactions

# ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
# [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]

class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self, key: int, val: int) -> Node:
        # create a new node with the key and value
        newNode = Node(key, val)
        # set that new node's next to the head
        newNode.next = self.head
        # if the head is not None, then set the head's prev to this new node
        if self.head is not None:
            self.head.prev = newNode
        # set the head pointer to the new Node
        self.head = newNode
        # if there was nothing in the queue to begin with, make this node also the tail
        if newNode.next is None:
            self.tail = newNode
            
        return newNode
        
        
    def remove(self, node: Node) -> int:
        # using the given node
        # if the node's next is not none, then set the next's prev to this node's prev
        if node.next is not None:
            node.next.prev = node.prev
        # else set tail to this node's prev 
        else:
            self.tail = node.prev
        # if the node's prev is not none, then set the prev's next to this node's next
        if node.prev is not None:
            node.prev.next = node.next
        # else set head to this node's next
        else:
            self.head = node.next
        
        return node.val
    
    
    def refresh(self, node: Node) -> int:
        returnVal = self.remove(node)
        self.add(node.key, node.val)        
        return returnVal
        
        
    def removeLU(self):
        removedKey = self.tail.key
        # if tail has a prev, set the tail's prev's next to be none and set tail to tail's prev
        if self.tail.prev is not None:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        # else set head to None and tail to None
        else:
            self.tail = None
            self.head = None
        
        return removedKey
    
    def printhead(self):
        print("head: " ,self.head.key, self.head.val)
    def printtail(self):
        print("tail: " ,self.tail.key, self.tail.val)
    def printfwd(self):
        cur = self.head
        ans = ""
        while cur:
            ans += "[" + str(cur.key) +" " +  str(cur.val) + "] -> "
            cur = cur.next
        print(ans)
    def printbwd(self):
        cur = self.tail
        ans = ""
        while cur:
            ans += " <- [" + str(cur.key) +" " +  str(cur.val) + "]"
            cur = cur.prev
        print(ans)

class LRUCache:
    def __init__(self, capacity: int):
        self.values = {}
        self.queue = Queue()
        self.capacity = capacity
        self.size = 0
        
    def get(self, key: int) -> int:
        # if theres nothing in that position, return -1
        if key not in self.values:
            return -1
        # move that node to the front of the queue and return it's value
        # returnVal = self.queue.refresh(self.values[key])
        # print("After get")
        # print(self.values.keys())
        # self.queue.printhead()
        # self.queue.printtail()
        # self.queue.printfwd()
        # self.queue.printbwd()
        # return returnVal
        return self.queue.refresh(self.values[key])
        

    def put(self, key: int, val: int) -> None:
        # Check if there is something at that value already
        # if yes, remove that node, and decrement the size
        if key in self.values:
            self.queue.remove(self.values[key])
            del self.values[key]
            self.size -= 1
            
        # add a node and increment the size
        self.values[key] = self.queue.add(key, val)
        self.size += 1
        # afterwards, check that the size is below the capacity
        if self.size > self.capacity:
            # if this is not the case, remove the value at the end of the queue
            removedKey = self.queue.removeLU()
            del self.values[removedKey]
            self.size -= 1
        # print("After put")
        # print(self.values.keys())
        # self.queue.printhead()
        # self.queue.printtail()
        # self.queue.printfwd()
        # self.queue.printbwd()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#third try, doesnt work

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        dummy = Node(-1)
        self.head = self.tail = dummy
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def refreshKey(self, key: int):
        print("Refreshing key: ",key)
        curF= self.head
        curB = self.tail
        while curF.val != key and curB.val != key:
            curF = curF.next
            curB = curB.prev
        
        if curF.val == key:
            newFront = curF
            prevNode = curF.prev
            nextNode = curF.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            newFront.next = self.head
            self.head.prev = newFront
            newFront.prev = None
            
        elif curB.val == key:
            newFront = curB
            prevNode = curB.prev
            nextNode = curB.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            newFront.next = self.head
            self.head.prev = newFront
            newFront.prev = None
                
        
        
    def addKey(self, key: int):
        print("Adding key: ",key)
        newFront = Node(key)
        newFront.next = self.head
        self.head.prev = newFront
        
    def deleteLU(self) -> int:
        if self.tail.val == -1:
            self.tail = self.tail.prev
            self.tail.next = None
            
        keyToRemove = self.tail.val
        self.tail = self.tail.prev
        self.tail.next = None
        return keyToRemove
        
        


class LRUCache:

    def __init__(self, capacity: int):
        self.queue = Deque()
        self.cache = {}
        self.size = 0
        self.cap = capacity
        

    def get(self, key: int) -> int:
        try:
            if self.cache[key]:
                self.queue.refreshKey(key)
                return self.cache[key]
        except:
            return -1
    
    def put(self, key: int, value: int) -> None:
        try:
            if self.cache[key]:
                self.queue.refreshKey(key)
                self.cache[key] = value
                return
        
        except:
            self.size += 1
            self.queue.addKey(key)
            if self.size > self.cap:
                keyToRemove = self.queue.deleteLU()
                del self.cache[keyToRemove]
            
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#second solution, terrible efficiency

class LRUCache:

    def __init__(self, capacity: int):
        # using hashmap and queue
        # space will be O(2N)
        
        #initialize linkedList head and tail
        self.cache = {}
        self.queue = []
        
        #initialize size
        self.size = 0
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.queue and self.cache[key]:
            # refresh key
            self.refreshKey(key)
            # hash key and find value
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.queue :
            self.size += 1
        # if at capacity, dequeue oldest key and remove from cache
        if self.size > self.capacity:
            removalKey = self.queue.pop(0)
            #print("popped key for removal: "+str(removalKey))
            del self.cache[removalKey] 
            #print("cache is now: ",self.cache)
            self.size -= 1
            
        # put key into queue
        if key in self.queue:
            self.refreshKey(key)
        else:
            self.queue.append(key)
        
        # using key, store value
        self.cache[key] = value
    
    def refreshKey(self, key: int) -> None:
        self.queue.append(self.queue.pop(self.queue.index(key)))


#first solution, doesnt work

class LRUCache:

    def __init__(self, capacity: int):
        # using hashmap and queue
        # space will be O(2N)
        
        #initialize linkedList head and tail
        self.map = [None] * (capacity+1)
        self.M = capacity+1
        self.queue = []
        
        #initialize size
        self.size = 0
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.queue:
            # refresh key
            self.queue.append(self.queue.pop(self.queue.index(key)))
            # hash key and find value
            return self.map[self.hashKey(key)] 
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.size += 1
        # if at capacity, dequeue oldest key and remove from map
        if self.size > self.capacity:
            removalKey = self.queue.pop(0)
            print("popped key for removal: "+str(removalKey))
            self.map[self.hashKey(removalKey)] = None
            print("map is now: ",self.map)
            self.size -= 1
            
        # put key into queue
        self.queue.append(key)
        
        # using key, store value
        self.map[self.hashKey(key)] = value
        
        
       
    def hashKey(self, key: int) -> int:
        return key % self.M
