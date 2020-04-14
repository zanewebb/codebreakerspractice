# second time

def maxArea(self, height: List[int]) -> int:        
        # two pointers, starting at each end
        left = 0
        right = len(height) - 1
        
        # store max area
        maxArea = -1
        
        # step one of the pointers inwards one at a time, moving the smaller of the two pointers
        while right != left:
            lowerHeight = height[left] if height[right] >= height[left] else height[right]
            
            maxArea = maxArea if maxArea > lowerHeight * (right - left) else lowerHeight * (right - left)
            
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        
        # when the pointers are equal, exit loop
        
        # return max
        return maxArea



# first time

def maxArea(self, height: List[int]) -> int:        
        # store max area, left pointer and right pointer
        maxArea = 0
        left = 0
        right = len(height)-1
        
        # for each pointer move, calculate the area which is the distance between pointers
        # and the height of the lower line (lower value at the pointer)
        # move the pointer with the lower array value towards the center
        # when the pointers are the same index, exit loop
        while left != right:
            checkArea = ( height[left] if height[left] < height[right] else height[right] ) * (right - left)
            if  checkArea > maxArea:
                maxArea = checkArea
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        # return the maxArea
        return maxArea