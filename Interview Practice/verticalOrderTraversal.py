# got it from memory noice
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        # dict of x coord : [nodes]
        seen = collections.defaultdict(list)
        
        # nodes will be tracked in tuples of (col, row, node)
        levelnodes = deque([(0, 0, root)])
        
        while len(levelnodes) > 0:
            col, row, node = levelnodes.popleft()
            
            # add to dict
            seen[col].append(node.val)
            
            if node.left:
                levelnodes.append((col-1, row+1, node.left))
            if node.right:
                levelnodes.append((col+1, row+1, node.right))
            
        ans = []
        for k in sorted(seen.keys()):
            ans.append(seen[k])
        
        # print(ans)
        return ans



#given solution, very close
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node_list = []

        def BFS(root):
            queue = deque([(root, 0, 0)])
            while queue:
                node, row, column = queue.popleft()
                if node is not None:
                    node_list.append((column, row, node.val))
                    queue.append((node.left, row + 1, column - 1))
                    queue.append((node.right, row + 1, column + 1))

        # step 1). construct the global node list, with the coordinates
        BFS(root)

        # step 2). sort the global node list, according to the coordinates
        node_list.sort()

        # step 3). retrieve the sorted results partitioned by the column index
        ret = OrderedDict()
        for column, row, value in node_list:
            if column in ret:
                ret[column].append(value)
            else:
                ret[column] = [value]

        return ret.values()

# first time, couldnt quite do it

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # dict of x-coord : [nodes]
        seen = collections.defaultdict(list)
        
        # should be tuples with (x,node)
        nodes = deque([(0,root)])
        
        while len(nodes) > 0:
            node = nodes.popleft()
            
            if node:
                # add the value to the answer dict
                seen[node[0]].append(node[1].val)
                
                # queue the next nodes
                if node[1].left:
                    nodes.append((node[0]-1, node[1].left))
                if node[1].right:
                    nodes.append((node[0]+1, node[1].right))
        
        
            # else:
            #     if len(nodes) > 0:
            #         nodes.append(None)
        
#         #seen[0].append(root.val)
#         self.look(0, root, seen)
        
        ans = []
        for k in sorted(seen.keys()):
            subans = []
            for n in seen[k]:
                subans.append(n)
            ans.append(subans)
        
        return ans
        
#     def look(self, x, node, seen):  
#         if node:
#             seen[x].append(node.val)
            
#             if node.left:
#                 self.look(x-1, node.left, seen)
        
#             if node.right:
#                 self.look(x+1, node.right, seen)
        