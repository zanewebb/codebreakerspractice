# had to look it up. brute force O(n) solution has a restriction on it

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dims = binaryMatrix.dimensions()
        r = 0
        c = dims[1]-1
        
        leftmost = 999999
        
        while r < dims[0] and c >= 0:
            val = binaryMatrix.get(r,c)
            if val == 1:
                leftmost = min(c, leftmost)
                c -= 1
            else:
                r += 1
        
        return leftmost if leftmost < 999999 else -1