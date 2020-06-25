
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