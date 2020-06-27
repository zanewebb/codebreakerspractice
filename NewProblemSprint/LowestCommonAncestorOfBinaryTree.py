# second time, still slow as hell
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.keypaths = []
    
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # do DFS
        self.DFS(root, [], p, q)
        
        # print(self.keypaths)
        
        # determine LCA
        pl, ql = self.keypaths[0], self.keypaths[1]
        seen = set()
        
        while len(pl) > 0 or len(ql) > 0:
            if len(pl) > 0:
                popped = pl.pop()
                if popped in seen:
                    # print(popped)
                    return popped
                seen.add(popped)
            if len(ql) > 0:
                popped = ql.pop()
                if popped in seen:
                    # print(popped)
                    return popped
                seen.add(popped)
        
        
    def DFS(self, node, path, p, q):
        if node:
            path.append(node)
            if node == p or node == q:
                self.keypaths.append(path[:]) 
        
            if node.left:
                self.DFS(node.left, path[:], p, q)
            if node.right:
                self.DFS(node.right, path[:], p, q)
        
        
        


# first time but 5% 5% LOL

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.p = None
        self.q = None
        self.paths = {}
    
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # store dict of int : list
        # we will later store the paths to p and q in there 
        # therefore, the dict should eventually be:
        '''
        {
            p.val: [nodes traversed to find p]
            q.val: [nodes traversed to find q]
        }
        '''
        
        self.p = p.val
        self.q = q.val
        
        # do a DFS search
        # after the DFS, the two paths should be set in the dict
        self.DFS(root, [])
        
        # iterate over both lists backwards
        # adding the values to two sets and checking if the node being added is already in the other set
        # the first time we find one that exists in the other, thats the lowest ancestor, return
        pl = self.paths[p.val]
        ql = self.paths[q.val]
        ps, qs = set(), set()
        i, j = len(pl)-1, len(ql)-1
        
        # print(self.paths)
        
        while True:
            if pl[i] in qs:
                return pl[i]
            if i >= 0:
                ps.add(pl[i])
                i -= 1
            
            if ql[j] in ps:
                return ql[j]
            if j >= 0:
                qs.add(ql[j])
                j -= 1
            
        
    
    def DFS(self, node, path):
        if node:
            path.append(node)
            if node.val == self.p:
                self.paths[self.p] = path
            if node.val == self.q:
                self.paths[self.q] = path
            
            self.DFS(node.left, path[:])
            self.DFS(node.right, path[:])
        
        