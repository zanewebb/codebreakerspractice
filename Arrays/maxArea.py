# fourth time

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        
        bestArea = -9999999
        while l < r:
            bestArea = max(( r - l  )* min(height[l], height[r]), bestArea)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return bestArea


# third time?

def maxArea(self, height: List[int]) -> int:        
        # two pointers, starting at each end
        l = 0
        r = len(height) - 1
        maxWater = 0
        
        while l<r:
            curWater = (r-l)* (height[l] if height[l] < height[r] else height[r])
            
            maxWater = max(maxWater, curWater)
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return maxWater

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