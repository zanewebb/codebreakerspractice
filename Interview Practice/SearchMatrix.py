
# fourth time, remembered linear search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        # start top right 
        col, row = len(matrix[0])-1, 0
        
        # while row counter is in bounds, and column counter is in bounds
        while row < len(matrix) and col >= 0:
            # if the value is too small, move down rows
            if matrix[row][col] < target:
                row += 1
            # elif the value is too big, move left
            elif matrix[row][col] > target:
                col -= 1
            else:
                return True
        
        return False

#third time, linear search
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m , n = len(matrix), len(matrix[0])
        r , c = 0, n-1
        
        
        # while the column is above or equal to 0
        # and while row is less than or equal to m
        while r < m and c >= 0:
            if matrix[r][c] < target:
                r += 1
            elif matrix[r][c] > target:
                c -= 1
            else:
                return True
        return Falses


# second time, recursive binary search
class Solution:    
    def __init__(self):
        self.matrix = None
        self.target = None
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        # assign class scope vars
        self.matrix = matrix
        self.target = target
        
        # kick off the recusive search with the scope of the search being the whole matrix
        return self.recursiveSearch(0, len(matrix)-1, 0 , len(matrix[0])-1)
    
    # recursive search that takes top bottom left and right
    def recursiveSearch(self,t, b, l, r): 
        # if the bounds of the array vertically or horizontally are overlapping then there are 
        # no cells to be searched in this sub matrix, return False
        if t > b or l > r:
            return False
        
        # if the value in the bottom right corner of this is too small for the target
        # or the top left corner is too big for the target, return false
        if self.matrix[t][l] > self.target or self.matrix[b][r] < self.target:
            return False
        
        # pick the midpoint of this sub-matrix with floor division
        midpoint =  l + (r - l) // 2
        
        # iterate down the column at the midpoint while the row is above or equal to the bottom boundary
        # and the value at the row, midpoint is less than or equal to the target
        row = t
        
        while row <= b and self.matrix[row][midpoint] <= self.target:
            # if the value at row,midpoint is the target, return true
            if self.matrix[row][midpoint] == self.target:
                return True
            row += 1
            
        # if we havent returned true yet, then we maxed out our row
        # continue recursive search
        return self.recursiveSearch(row, b, l, midpoint-1) or self.recursiveSearch(t, row-1, midpoint+1, r)
        
    


# brute force inefficient solution
def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        #move diagonally inwards, each time we encounter a number too small
        i = j = 0
        while i < len(matrix) and j < len(matrix[i]):
            if matrix[i][j] < target:
                # iterate right until we exceed or find the target
                n, m = i, j
                while m < len(matrix[i]):
                    if matrix[i][m] == target:
                        return True
                    elif matrix[i][m] < target:
                        m += 1
                    else:
                        break
                while n < len(matrix):
                    if matrix[n][j] == target:
                        return True
                    elif matrix[n][j] < target:
                        n += 1
                    else:
                        break
                
                i += 1
                j += 1                    

                # iterate down until we exceed or find the target
            elif matrix[i][j] == target:
                return True
            else:
                return False
            
        return False