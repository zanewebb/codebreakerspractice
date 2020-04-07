

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
