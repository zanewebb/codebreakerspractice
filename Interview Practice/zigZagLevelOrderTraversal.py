# third time
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        movingright = True
        
        levelnodes = deque([root,None])
        
        levelvalues = deque()
        
        ans = []
        
        while len(levelnodes) > 0:
            popped = levelnodes.popleft()
            
            if popped:
                if popped.left:
                    levelnodes.append(popped.left)
                if popped.right:
                    levelnodes.append(popped.right)
                if movingright:
                    levelvalues.append(popped.val)
                else:
                    levelvalues.appendleft(popped.val)
                
            else:
                ans.append(levelvalues)
                levelvalues = deque()
                
                if len(levelnodes) > 0:
                    levelnodes.append(None)
                    
                movingright = not movingright
        return ans
                
        
        
        


# second time?
# almost had it, forgot to preload the level delimiter / when to add new ones

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        levels = []
        movingLeft = True
        levelVals = deque()
        levelNodes = deque([root,None])
        
        while len(levelNodes) > 0:
            node = levelNodes.popleft()
            
            if node:
                if node.left:
                    levelNodes.append(node.left)
                if node.right:
                    levelNodes.append(node.right)
                if movingLeft:
                    levelVals.append(node.val)
                else:
                    levelVals.appendleft(node.val)
            
            else:
                levels.append(levelVals)
                levelVals = deque()
                
                # if there are more to look at , add a level delimiter
                if len(levelNodes) > 0:
                    levelNodes.append(None)
                    
                movingLeft = not movingLeft
            
        return levels
            



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