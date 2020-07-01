# second time, good
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.values = []
        self.i = 0
        
        if root:
            self.DFS(root)
            
        self.values = sorted(self.values)

    def DFS(self, node):
        self.values.append(node.val)
        
        if node.left:
            self.DFS(node.left)
        if node.right:
            self.DFS(node.right)
    
    def next(self) -> int:
        """
        @return the next smallest number
        """
        res = self.values[self.i]
        self.i += 1
        return res

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.i < len(self.values) else False
        

# way simpler way
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.values = []
        self.DFS(root)
        self.i = -1
        
        self.values = sorted(self.values)
        
        
    def DFS(self, node):
        if node:
            self.values.append(node.val)
            if node.left:
                self.DFS(node.left)
            if node.right:
                self.DFS(node.right)
    
    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.i += 1
        #print("returning:",self.values[self.i] )
        return self.values[self.i]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.i < len(self.values)-1 else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()



# bad non solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.parents = {}
        # self.hasNext = False
        self.cur = root
        self.seen = set()
        self.size = 0
        
        # if root.left:
        #     self.parents[root.left] = root
        # if root.right:
        #     self.parents[root.right] = root
        self.DFS(root)
        
        while self.cur.left:
            self.cur = self.cur.left
        
    def DFS(self, node):
        self.size += 1
        if node.left:
            self.parents[node.left] = node
            self.DFS(node.left)
        if node.right:
            self.parents[node.right] = node
            self.DFS(node.right)
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        # if len(self.seen) == 0:
        #     self.seen.add(self.cur)
        #     return self.cur.val
        
        while self.cur in self.seen and self.size > len(self.seen):
            if self.cur.left and self.cur.left not in self.seen:
                self.cur = self.cur.left
            elif self.cur.right and self.cur.right not in self.seen:
                self.cur = self.cur.right
            elif self.cur in self.parents and self.parents[self.cur] not in self.seen:
                self.cur = self.parents[self.cur]
            print("looking at:",self.cur.val)
        
        self.seen.add(self.cur)
        print("returned",self.cur.val)
        return self.cur.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.size > len(self.seen) else False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()