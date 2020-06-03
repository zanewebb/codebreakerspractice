
# second time
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root, -99999999999, 99999999999)
    
    def validate(self, node, minval, maxval):
        # if this node is none, return true
        if not node:
            return True
        # if the node's val is smaller than min or greater than max, return false
        if node.val < minval or node.val > maxval:
            return False
        
        # recursive case
        # recursively call with max as this node's val - 1
        # recursively call with min as this node's val + 1
        return self.validate(node.left, minval, node.val - 1) and self.validate(node.right, node.val + 1, maxval)
        
        



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True
        
        return self.DFS(root, -999999999999, 99999999999999)
        
    def DFS(self, node: TreeNode, minval, maxval):
        if not node:
            return True
        if node.val < minval or node.val > maxval:
            return False
        else:
            return self.DFS(node.left, minval, node.val - 1) and self.DFS(node.right, node.val + 1, maxval)
        
        