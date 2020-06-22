
#not the cleanest but i got it without looking it up again

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        self.trickle(root,limit)
        
        if not root.left and not root.right:
            return None
        
        return root
    
    
    def trickle(self, node, rollingsum):
        rollingsum = rollingsum - node.val
        # its a leaf
        if not node.left and not node.right:
            # valid or not valid
            if rollingsum <= 0:
                return node
            else:
                return None
        if node.left:
            node.left = self.trickle(node.left, rollingsum )
        
        if node.right:
            node.right = self.trickle(node.right, rollingsum)
        
        if not node.left and not node.right:
            return None
        
        return node



# easier to comprehend solution, same idea
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if not root:
            return None
        
        # if we're at a leaf and the leaf makes this branch valid, return it so that it is preserved
        if not root.right and not root.left and root.val >= limit:
            return root
        
        # double check that the branch is there, then recusively search and/or strip that branch
        if root.right:
            root.right = self.sufficientSubset(root.right, limit - root.val)
        if root.left:
            root.left = self.sufficientSubset(root.left, limit - root.val)
        
        # if there are still dependent other branches, then do not remove this node
        if root.right or root.left:
            return root
        else:
            # otherwies, continue removing this branch
            return None



# dang im stupid
# this is the accepted solution

def sufficientSubset(self, root, limit):
        if root.left == root.right:
            return None if root.val < limit else root
        if root.left:
            root.left = self.sufficientSubset(root.left, limit - root.val)
        if root.right:
            root.right = self.sufficientSubset(root.right, limit - root.val)
        return root if root.left or root.right else None