
# first try

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        levelnodes = deque([root, None])
        levelvalues = []
        output = []
        
        while len(levelnodes) > 0:
            node = levelnodes.popleft()
            
            if node:
                if node.left:
                    levelnodes.append(node.left)
                if node.right:
                    levelnodes.append(node.right)

                levelvalues.append(node.val)
            
            else:
                output.append(levelvalues)
                levelvalues = []
                if len(levelnodes) > 0:
                    levelnodes.append(None)
        
        return output