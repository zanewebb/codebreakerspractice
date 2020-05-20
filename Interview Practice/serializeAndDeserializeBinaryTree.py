# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# my bastardized recalled solution after having read it once days before. Much cleaner
# to just pop off the indicies of the data list instead of tracking an index


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        
        return self.ser(root,"")
    
    def ser(self, node, ser):
        if not node:
            ser += "None,"
        
        else:
            ser += str(node.val) + ","
            ser = self.ser(node.left, ser)
            ser = self.ser(node.right, ser)
            
        return ser
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data.split(",")[:-1])
        root = self.des(data.split(",")[:-1], 0)
        return root[0]
        
    def des(self, nodes , ind) -> (TreeNode, int): 
        if ind >= len(nodes):
            return
        
        if nodes[ind] == "None":
            return (None, ind + 1)
        
        # create the new TreeNode
        newNode = TreeNode(nodes[ind])
        res = self.des(nodes, ind + 1)
        newNode.left, rightInd = res[0], res[1] 
        res = self.des(nodes, rightInd)
        newNode.right, nextInd = res[0], res[1] 
        return (newNode, nextInd)
        
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))