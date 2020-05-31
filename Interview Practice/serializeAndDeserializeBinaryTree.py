# second time, holy crap im bad    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Doesnt work
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return self.ser(root, "")
        
    def ser(self, node, serstring):
        if not node:
            return serstring +",None"
        else:
            return "," + str(node.val) + self.ser(node.left, serstring) + self.ser(node.right, serstring)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodeList = data.split(",")[1:]
        print(nodeList)
        root = TreeNode(nodeList[0])
        rightInd = self.des(root, nodeList, 1 )
        self.des(root, nodeList, rightInd )
        return root
        
        
    def des(self, node, nodeList, ind):
        if ind < len(nodeList) and nodeList[ind] != "None":
            node.left = TreeNode(nodeList[ind])
            rightInd = self.des(node.left, nodeList, ind + 1)
            
            if rightInd < len(nodeList) and nodeList[rightInd] != "None":
                node.right = TreeNode(nodeList[rightInd])
                nextInd = self.des(node.right, nodeList, rightInd + 1)
                print("on ind",ind,"returning nextInd",nextInd)
                return nextInd
            else:
                print("on ind",ind,"returning rightInd",rightInd+1)
                return rightInd + 1
                
        else:
            print("on ind",ind,"returning ind",ind+1)
            return ind + 1
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


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