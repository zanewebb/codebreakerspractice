
# fourth time
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.rightside = {}
        
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.DFS(root, 0)
        return self.rightside.values()
        
    
    def DFS(self, node, depth):
        if node:
            if depth not in self.rightside:
                self.rightside[depth] = node.val
            
            self.DFS(node.right, depth+1)
            self.DFS(node.left, depth+1)
        



# third time? EZ PZ
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodes = {}
        
        
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root:
            self.DFS(root, 0)
        return self.nodes.values()
    
    def DFS(self, node, depth):
        if depth not in self.nodes:
            self.nodes[depth] = node.val
        
        if node.right:
            self.DFS(node.right, depth + 1)
        if node.left:
            self.DFS(node.left, depth + 1)
        
        
        
        


# does work, need to do right side traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        # dict of row: rightmost node (tuple of (col,node.val))
        self.rightnodes = {}
    
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        self.DFS(0, 0, root)
        # print(self.rightnodes)
        # dissolve rightnodes dict values into one list
        ans = []
        for k in sorted(self.rightnodes.keys()):
            ans.append(self.rightnodes[k][1])
        
        return ans
        
    def DFS(self, row, col, node):
        if row not in self.rightnodes:
            self.rightnodes[row] = (col, node.val)
        # elif self.rightnodes[row][0] <= col:
        #     self.rightnodes[row] = (col, node.val)
        
        if node.right:
            self.DFS(row + 1, col + 1, node.right)
        if node.left:
            self.DFS(row + 1, col - 1, node.left)
        
        

# doesnt work

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        # dict of row: rightmost node (tuple of (col,node.val))
        self.rightnodes = {}
    
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        self.DFS(0, 0, root)
        # print(self.rightnodes)
        # dissolve rightnodes dict values into one list
        ans = []
        for k in sorted(self.rightnodes.keys()):
            ans.append(self.rightnodes[k][1])
        
        return ans
        
    def DFS(self, row, col, node):
        if row not in self.rightnodes:
            self.rightnodes[row] = (col, node.val)
        elif self.rightnodes[row][0] <= col:
            self.rightnodes[row] = (col, node.val)
        
        if node.left:
            self.DFS(row + 1, col - 1, node.left)
        if node.right:
            self.DFS(row + 1, col + 1, node.right)
        
        