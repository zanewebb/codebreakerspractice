# third time, still couldnt get it
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colorednodes = {}
        color = -1
        
        # iterate over the graph nodes, just the indexes since
        # the index represent's the node's value
        for n in range(len(graph)):
            # if the node isnt in the dict of colored nodes then begin DFS
            if n not in colorednodes:
                # the DFS works by adding new nodes to a stack and coloring them 
                # until there are no nodes left in the stck
                stack = [n]
                colorednodes[n] = color
                
                while len(stack) > 0:
                    node = stack.pop()
                    # iterate over the connections to this node (found in the given graph)
                    for nodeconnection in graph[node]:
                        # if we havent seen it, add it to ou DFS stack
                        if nodeconnection not in colorednodes:
                            stack.append(nodeconnection)
                            colorednodes[nodeconnection] = colorednodes[node] * -1
                        # if we've seen it and it matches the color of the node we're on, return false
                        elif colorednodes[nodeconnection] == colorednodes[node]:
                            return False
        return True
            
            
        


# second time, couldnt get it again, 76/78 cases
# gotta do it the stupid stack way

class Solution:
    def __init__(self):
        self.nodes = {}
        self.graph = None
        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        nodes = {}
        self.graph = graph
        
        res = True
        for g in graph:
            if g:
                res = self.DFS(g, -1)
                break
        print(self.nodes)
        return res
        
        
    def DFS(self, node, color):
        # print("checking node", node)
        # if not node:
        #     return False
        
        good = True
        for n in node:
            if n in self.nodes:
                if self.nodes[n] != color:
                    return False
            else:
                # print("assigning color", color, "to node", n)
                self.nodes[n] = color
                good = good and self.DFS(self.graph[n], color * -1)
        
        # print(self.nodes, good)
        return good
    
        


# had no idea how to do this

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # mark the nodes with "colors" -1 or 1
        nodecolors = {}
        
        # the index of the list represents the number of the node
        for node in range(len(graph)):
            # if this is an unvisited node, do a DFS on this node
            if node not in nodecolors:
                stack = [node] # this adds a whole list of connected nodes
                nodecolors[node] = 1
                
                # DFS in this scenario just means that we access the connections of a node
                # via the given graph list
                while len(stack) > 0:
                    popped = stack.pop()
                    
                    # iterate over the connections of the node we popped from our stack
                    for n in graph[popped]:
                        # if we havent colored this node yet, color it
                        # by setting it to the opposite color of the current color
                        # - we also make sure to add this node to the stack of nodes
                        # to continue invsetigating
                        if n not in nodecolors:
                            stack.append(n)
                            nodecolors[n] = nodecolors[popped] * -1
                        
                        # if the node we're checking has already been colored
                        # and its color is the same as the node before this 
                        # then it is in violation of the alternating rule
                        elif nodecolors[n] == nodecolors[popped]:
                            return False
                        
        return True