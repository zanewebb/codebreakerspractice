# almost got it from memory, not quite on the "break" and final edge case check
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        indegrees = Counter({c:0 for word in words for c in word})
        adj = defaultdict(set)
        
        for w1, w2 in zip(words[:-1], words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indegrees[c2] += 1
                    break
            else:
                # cover edgecase for faulty input
                if len(w2) < len(w1):
                    return ""
                
        # print(adj, indegrees)
        
        order = []
        queue = deque([c for c in indegrees if indegrees[c] == 0 ])
        
        while queue:
            c = queue.popleft()
            order.append(c)
            for n in adj[c]:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    queue.append(n)
        
        if len(order) < len(indegrees):
            return ""
        
        return "".join(order)


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # create adjacency list with dict of sets
        adj = defaultdict(set)
        
        # create and populate a counter
        # indegree means how many nodes point to a given node
        # we need to track the indegree of each node so we know which nodes to pop first
        # as we build out our final order
        indegree = collections.Counter()
        for w in words:
            for c in w:
                indegree[c] = 0
        
        # visiting each word, comparing it to the following word
        for i in range(0, len(words)-1):
            for c1, c2 in zip(words[i], words[i+1]):
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indegree[c2] += 1
                    break
                    
            # didn't know you could slap else conditions after a for loop if the for loop didnt run
            # this checks if theres an edge case condition where the second word is a prefix of the first
            else:
                if len(words[i+1]) < len(words[i]):
                    return ""
        
        outputOrder = []
        # queue because this approach is for picking off any nodes with indegree of 0 over and over
        queue = []
        for c in indegree:
            if indegree[c] == 0:
                queue.append(c)
        queue = deque(queue)
        
        # while there are still nodes left to process
        while queue:
            # it is important to pop left because the order that we added them to the
            # indegree counter was lexigraphically correct initially, we must preserve this order
            c1 = queue.popleft() 
            outputOrder.append(c1)
            for c2 in adj[c1]:
                # now that we've popped the node with an indegree of 0, we decrement the indregree of any nodes that 
                # were adjacent since it is no longer pointing to those nodes
                indegree[c2] -= 1
                if indegree[c2] == 0:
                    queue.append(c2) # if the indegree hit 0 then this node is a target for being popped next
        
        # if the output order is less than the total number of letters then we missed some
        # this has to have been from a cycle in the graph and therefore the order given was invalid
        if len(outputOrder) < len(indegree):
            return ""
        
        return "".join(outputOrder)
        
        
        
        
        
        
        
        