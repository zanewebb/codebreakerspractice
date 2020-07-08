# eighth time
class Solution:
    def __init__(self):
        self.depths = None
        self.nodes = collections.defaultdict(list)
        self.ans = []
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.depths = [-1] * n
        
        for conn in connections:
            self.nodes[conn[0]].append(conn[1])
            self.nodes[conn[1]].append(conn[0])
        
        self.DFS(-1, connections[0][0], 0)
        
        return self.ans
        
    def DFS(self, parent, current, depth):
        self.depths[current] = depth
        
        # look at each connection on this node
        for n in self.nodes[current]:
            if n == parent:
                continue # dont go right back to the node we just visited
            
            # if we havent visited this node then continue looking
            if self.depths[n] < 0:
                self.DFS(current, n, depth + 1)
                self.depths[current] = min(self.depths[current], self.depths[n])
            
            # otherwise we've already seen it so just update the depth on this node
            else:
                self.depths[current] = min(self.depths[current], self.depths[n])
        
        if self.depths[current] == depth and parent != -1:
            self.ans.append([parent,current])
        
        
        

# seventh time
class Solution:
    def __init__(self):
        self.nodes = collections.defaultdict(list)
        self.depths = None
        self.ans = []
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.depths = [-1] * n
        
        for c in connections:
            self.nodes[c[0]].append(c[1])
            self.nodes[c[1]].append(c[0])
        
        self.DFS(connections[0][0], -1, 0)
        
        return self.ans
        
    def DFS(self, current, parent, depth):
        self.depths[current] = depth
        
        for n in self.nodes[current]:
            if n == parent:
                continue
            if self.depths[n] < 0:
                self.DFS(n, current, depth + 1)
                self.depths[current] = min(self.depths[current], self.depths[n])
            else:
                self.depths[current] = min(self.depths[current], self.depths[n])
        
        if self.depths[current] == depth and parent != -1:
            self.ans.append([current,parent])
        
        
        


# sixth time

class Solution:
    def __init__(self):
        self.nodes = None
        self.depths = None
        self.ans = []
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # assign depths with n
        self.depths = [-1] * n
        
        # create adjacency list
        self.nodes = collections.defaultdict(set)
        for conn in connections:
            self.nodes[conn[0]].add(conn[1])
            self.nodes[conn[1]].add(conn[0])
        
        print(self.nodes)
        # begin DFS
        self.DFS(connections[0][0], -1, 0)
        
        print(self.depths)
        # return ans list
        return self.ans
        
        
    def DFS(self, current, parent, depth):
        # update the depth of the current
        self.depths[current] = depth
        print(self.depths)

        # iterate over its children
        for n in self.nodes[current]:
            # if the child is the same as the parent, dont DFS
            if n == parent:
                continue
            # dfs with the child node if the node has not been visited before
            if self.depths[n] == -1:
                self.DFS(n, current, depth + 1)
            # update the depth of this node to the min of its current depth or the depth of the child
            self.depths[current] = min(self.depths[current], self.depths[n])
            
        # if the depth for this node is still the same as the given depth, it is critical, add it to ans
        if self.depths[current] == depth and parent != -1:
            self.ans.append([current,parent])

# fifth time, got it after some minor debugs
class Solution:
    def __init__(self):
        self.depths = None
        self.nodes = None
        self.ans = []
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.depths = [-1] * n
        self.nodes = collections.defaultdict(set)
        for conn in connections:
            self.nodes[conn[0]].add(conn[1])
            self.nodes[conn[1]].add(conn[0])
        
        self.DFS(connections[0][0], -1, 0)
        
        return self.ans
    
    def DFS(self, current, parent, depth):
        # set the depth value now that we've arrived at this node
        self.depths[current] = depth
        
        # iterate over linked nodes
        for n in self.nodes[current]:
            # make sure to skip the DFS if we just came from that node
            if n == parent:
                continue
            
            # if we havent seen it, perform the DFS
            if self.depths[n] == -1:
                self.DFS(n, current, depth + 1)
                
                # update the depth for this node to see if it ended in a cycle
                self.depths[current] = min(self.depths[n], self.depths[current])
                
            # if we have seen it, just update the depth for this node
            else:
                self.depths[current] = min(self.depths[n], self.depths[current])
        
        # before leaving this node, see if the DFS after this node updated the depth value
        # this would make it a critical connection if it did not
        if self.depths[current] == depth and parent != -1:
            self.ans.append([current, parent])

# fourth time, so close to a clean implementation

# it is critical that we CONTINUE if we encounter a parent. This should ALSO remind me that the parent check is part of the 
# FOR LOOP and not outside of it.

class Solution:
    def __init__(self):
        self.depths = None
        self.nodes = None
        self.ans = []
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.depths = [-1] * n
        
        # populate the adjacency dict for the nodes
        self.nodes = collections.defaultdict(set)
        for con in connections:
            self.nodes[con[0]].add(con[1])
            self.nodes[con[1]].add(con[0])
        
        # kick off the search
        self.DFS(connections[0][0], -1, 0)
        
        # return our answer
        return self.ans
    
    def DFS(self, cur, par, depth):
        self.depths[cur] = depth
        
        # for each child of this node (linked node)
        for n in self.nodes[cur]:
            # first make sure that this current is not where we just came from
            if n == par:
                continue
                
            # if we have not visited this node yet
            if self.depths[n] == -1:
                # dive deeper
                self.DFS(n,cur,depth+1)
                
            # when that comes back, update our depth for THIS node
            self.depths[cur] = min(self.depths[cur], self.depths[n])
        
        # now we check to see whether or not this connection is critical
        if self.depths[cur] == depth and par != -1:
            self.ans.append([cur, par])
        
        

# third ? time, found a slightly cleaner way to complete this tarjan algorithm
class Solution:
    
    def __init__(self):
        self.ans = []
        self.nodes = None
        self.dists = None
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.dists = [-1]*n
        self.nodes = collections.defaultdict(set)
        
        # create the dict with sets of the connected nodes for each node
        for conn in connections:
            self.nodes[conn[0]].add(conn[1])
            self.nodes[conn[1]].add(conn[0])
        
        print(self.nodes)
            
        # begin the DFS with the first node in the first connections, no parent, a dist of 0
        self.DFS(connections[0][0], -1, 0)
        
        return self.ans
        
    def DFS(self, current, parent, dist):
        self.dists[current] = dist
        
        for n in self.nodes[current]:
            # base case where we have mistakenly continued the DFS back to where we just were
            if n == parent:
                continue
            # if we havent visited this, continue the search
            if self.dists[n] == -1:
                self.DFS(n, current, dist + 1)
                
                # update the dist for this node
                self.dists[current] = min(self.dists[current], self.dists[n])
            # ELSE, if we have already seen this node, then kindly update the curent node to the smaller 
            # of the two dists
            else:
                self.dists[current] = min(self.dists[current], self.dists[n])
        # determine if it's critical by checking if it found a loop
        # we can tell if it was a loop by seeing whether or not the dist was updated after
        # the DFS recursion came back from earlier.
        if self.dists[current] == dist and parent != -1:
            self.ans.append([current, parent])


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