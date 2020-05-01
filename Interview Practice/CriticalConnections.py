class Solution:


   # proper algorithm with, tricky implementation, need more practice
   def __init__(self):
        self.ans = []
        self.links = None
        self.nodes = None
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # generate default links ints to work as a tracker for if we've seen the nodes
        # and to track the lowest link number for each node, which will ID cycles
        self.links = [-1] * n
        
        # create adjacency dict
        self.nodes = collections.defaultdict(set)
        for conn in connections:
            self.nodes[conn[0]].add(conn[1])
            self.nodes[conn[1]].add(conn[0])
        #print(self.nodes)
        #print(connections[0][0])
        
        # launch DFS
        self.DFS(connections[0][0],-1, 0)
        
        return self.ans
        
    def DFS(self, current, parent, linkNum):
        self.links[current] = linkNum
        
        for node in self.nodes[current]:
            # if we're backtracking, ignore
            if node == parent:
                continue
            # if we havent seen the node before
            if self.links[node] == -1:
                # continue the search
                smallestLink = self.DFS(node, current, linkNum+1)
                # update the link for this spot if we found something smaller (cycle somewhere)
                self.links[current] = min(smallestLink, self.links[current])
            else:
                self.links[current] = min(self.links[node], self.links[current])
        
        # after we've completed the DFS for each node that is a child of this one
        # either the link for this node has been updated and it isnt critical (because there was a cycle)
        # or the link was not updated for this meaning that [current, parent] is the only edge between the two nodes
        if self.links[current] == linkNum and parent != -1:
            self.ans.append([current, parent])
        
        # we return what we have here for consideration of nodes that are parents of this one.
        return self.links[current]




   # misunderstood the full criteria for a critical server, solution doesnt match the problem


    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # dict storing the server number and count of connections
        connection_counts = collections.Counter()
        # iterate over the connections list and tally up the number of connections for each server
        for conn in connections:
            connection_counts[conn[0]] += 1
            connection_counts[conn[1]] += 1
        # find any connections where there is a server number that has only one connection
        critical_connections = dict(filter(lambda server: server[1] == 1, connection_counts.items()))
        #print(critical_connections)
        ans = filter(lambda conn: conn[0] in critical_connections or conn[1] in critical_connections, connections)
        # return that list
        return ans