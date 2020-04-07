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