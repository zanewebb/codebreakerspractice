
'''
Critical Connections
'''
'''
Given an underected connected graph with n nodes labeled 1..n. A bridge (cut edge) is defined as an edge which,
when removed, makes the graph disconnected (or more precisely, increases the number of connected components
in the graph). Equivalently, an edge is a bridge if and only if it is not contained in any cycle. The task is to
find all bridges in the given graph. Output an empty list if there are no bridges.
Input:
n, an int representing the total number of nodes.
edges, a list of pairs of integers representing the nodes connected by an edge.
'''
# Example 1:
# Input:
# n = 5
# edges = [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]
# Output: [[1, 2], [4, 5]]
# Explanation:
# There are 2 bridges:
# 1. Between node 1 and 2
# 2. Between node 4 and 5
# If we remove these edges, then the graph will be disconnected.
# If we remove any of the remaining edges, the graph will remain connected.
#
# Example 2:
# Input:
# n = 6
# edges = [[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [4, 6], [5, 6]]
# Output: []
# Explanation:
# We can remove any edge, the graph will remain connected.
#
# Example 3:
# Input:
n = 9
edges = [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]]
# Output: [[3, 4], [3, 6], [4, 5]]

import collections
def criticalConnections(n, connections):
   # create and populate a dictionary of nodes with sets of nodes that they connect to
   # (adjacency list) ?
   dic = collections.defaultdict(set)
   for u, v in connections:
      dic[u].add(v)
      dic[v].add(u)
   print(dic)

   # populate a list of values to indicate their lowest connected node
   # this also acts as an indicator for whether or not they have been visited already
   steps = [-1 for i in range(n + 1)]

   # answer set
   res = []

   # begin depth first search
   helper(1, -1, 0, steps, dic, res) # starting node number, parent (none),, level counter, pointers to critical resources
   return res

def helper(cur, par, level, steps, dic, res):
   # temporarily update the steps in the index that represents this node
	steps[cur] = level

   # initiate a search on each connected node for this node
	for child in dic[cur]:
      # if we just came from the node that we're now evaluating, do not bother with a search, move on
		if child == par:
			continue

      # if we have not visited it yet
		if steps[child] == -1:
         # continue looking. Eventually this will come back returning the lowest level / step it encountered. 
         # if it comes back with something higher than what we're currently at, we know that this is a critical connection
			min_step = helper(child, cur, level + 1, steps, dic, res)

         # now that it has come back, choose the lower of the two, our current level, or the one that the DFS ended up with.
			steps[cur] = min(steps[cur], min_step)
		else:
         # if we have encountered this node already, we've hit a cycle. update our step / level at this index
         # to  the smaller of the two 
			steps[cur] = min(steps[child], steps[cur])

   # if after running those recursive depth searches didn't update our current step to be lower (different) than our initial given level
   # then this edge between current and parent must be a critical connection
	if steps[cur] == level and cur != 0 and par != -1:
		res.append([cur, par])
   
   # whatever the resolution was, report out what our level / step is so that outer calls of our search can
   # update their steps and therefore determine if they themselves are critical edges.
	return steps[cur]

# n = 4
# edges = [[0,1],[1,2],[2,0],[1,3]]
print(criticalConnections(n, edges))