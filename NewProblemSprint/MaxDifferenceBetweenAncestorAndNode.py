
# incredible solution
def maxAncestorDiff(self, root, mn=100000, mx=0):
        return max(self.maxAncestorDiff(root.left, min(mn, root.val), max(mx, root.val)), \
            self.maxAncestorDiff(root.right, min(mn, root.val), max(mx, root.val))) \
            if root else mx - mn


# works but super inefficient

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        # 
        return self.maxdiff(root, [])
    
    def maxdiff(self, node, path):
        # print(node.val)
        # print(path)
        bestdiff = -1
        if path:
            bestdiff = abs(max(node.val,max(path)) - min(node.val, min(path)))
        path.append(node.val)
        
        if node.left:
            bestdiff = max(bestdiff, self.maxdiff(node.left, path[:]))
        if node.right:
            bestdiff = max(bestdiff, self.maxdiff(node.right, path[:]))
        
        return bestdiff