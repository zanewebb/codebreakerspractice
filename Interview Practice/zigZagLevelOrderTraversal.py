# shaky on understandig of this, need practice on BFS thinking



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None
        
        # there will be a return list
        ans = []
        # deque of encountered values for the current level
        level_values = deque()
        # deque of nodes encountered with None as a delimiter for levels
        nodes = deque([root,None])
        # boolean determining left to right or right to left
        r2l = True
        
        while len(nodes) > 0:
            cur = nodes.popleft()
            
            # if we arent at the end of a level, proceed
            if cur:
                # depending on our direction, we must store the vals in our deque differently
                if r2l:
                    level_values.append(cur.val)
                else:
                    level_values.appendleft(cur.val)
                
                # we must log the nodes that we encountered for the next level
                if cur.left:
                    nodes.append(cur.left)
                if cur.right:
                    nodes.append(cur.right)
        
            # if the popped val is none, we hit the end of this level
            else:
                # append the level_values to the ans and clear the level_values
                ans.append(level_values)
                level_values = deque()
                
                # if there are still more nodes to traverse, add a level delimiter 
                if len(nodes) > 0:
                    nodes.append(None)
                
                # switch the direction for the next level
                r2l = not r2l
                
        return ans