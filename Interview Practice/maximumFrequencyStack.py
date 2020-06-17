# third time, got it
class FreqStack:

    def __init__(self):
        # val: freq
        self.freqs = {}
        
        # freq: [vals]
        self.vals = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x: int) -> None:
        # get the existing frequency or provide 0
        self.freqs[x] = self.freqs.get(x, 0) + 1
        
        self.maxfreq = max(self.maxfreq, self.freqs[x])
        
        # add it to its respectivee frequency stack
        self.vals[self.freqs[x]].append(x)

    def pop(self) -> int:
        popped = self.vals[self.maxfreq].pop()
        if len(self.vals[self.maxfreq]) == 0:
            self.vals.pop(self.maxfreq)
            
        if len(self.vals.keys()) > 0:
            self.maxfreq = max(self.vals.keys())
        else:
            self.maxfreq = 0
            
        self.freqs[popped] -= 1
        
        return popped



# second time, tricky, had to carefully think through my issues i was having but got it
class FreqStack:

    def __init__(self):
        # dict of elem: freq
        self.freqs = collections.Counter()
        
        # dict of freq: stack
        self.values = collections.defaultdict(list)
        
        self.maxfreq = 0
        '''
                # freqs
                {
                   1: 2
                   2: 1
                }

                # values
                {
                    2: [1]
                    1: [1, 2]
                }

                # maxfreq
                1


        '''
        
    def push(self, x: int) -> None:
        self.freqs[x] += 1
        self.values[self.freqs[x]].append(x)
        self.maxfreq = max(self.maxfreq, self.freqs[x])

    def pop(self) -> int:
        # pop the max freq value
        popped = self.values[self.maxfreq].pop()
        
        # decrement the frequency
        self.freqs[popped] -= 1
        
        if len(self.values[self.maxfreq]) == 0:
            self.values.pop(self.maxfreq, None)
        self.maxfreq = max(self.values.keys()) if len(self.values.keys()) > 0 else 0
        return popped




# wow
# approved solution
class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self):
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x

# my very bad try
# tried to do a max heap and a stack and anwdkjnawkdnawdjuhnaiuwdijun
import heapq
class FreqStack:

    def __init__(self):
        self.stack = []
        
        # filled with tuples:
        # (count, element)
        self.values = []
        # counts should be 
        # element : count
        self.valset = set()
    def push(self, x: int) -> None:
        self.stack.append(x)
        if x in self.valset:            
            for t in self.values:
                if t[1] == x:
                    t[0] -= 1
                    heapq.heapify(self.values)
                    break
        else:
            heapq.heappush(self.values, (-1, x))
                
    def pop(self) -> int:
        # get the highest frequency element
        highestCount = heapq.heappop(self.values)
        fewestElems = {}
        while len(self.values) > 0 and self.values[0] == highestCount:
            elem = heapq.heappop(self.values)
            fewestElems[elem[1]] = elem
        
        # identify the specific val to pop
        returnelem = None
        for i in range(len(self.stack), -1, -1):
            if not returnelem and self.stack[i] in fewestElems:
                returnelem = self.stack[i]
                # decrement the frequency of this element
                fewestElems[returnelem][0] += 1
                self.stack.pop(i)
        
        
        # re-add any remaining elems to the heap
        readd = fewestElems.values()
        while len(readd) > 0:
            elem = readd.pop()
            if elem[0] < 0:
                heapq.heappush(self.values, elem)
                self.valset.discard(elem[1])
        
        return returnelem


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()