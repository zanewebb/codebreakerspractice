#maxSubArray

# fifth time, forgot what the super elegant solution was 
def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # track current max and best max
        curMax, bestMax = 0, -99999999999999999
        for i in range(0,len(nums)):
            curMax += nums[i]
            
            bestMax = max(bestMax, curMax)
            
            if curMax < 0:
                curMax = 0
        
        return bestMax

# super elegant solution
for i in range(1,len(nums)):
        nums[i] = max(nums[i], nums[i-1] + nums[i])
return max(nums)


# fourth time

def maxSubArray(self, nums: List[int]) -> int:
        # track best max and current max
        bestMax = -9999999999
        curMax = 0
        # iterate over nums
        for n in nums:
            # add current num to current max
            curMax += n
            # if current max is bigger than best max, set it
            bestMax = max(curMax, bestMax)
            # if current max is less than 0, reset to 0
            curMax = max(0, curMax)
        # return best max
        return bestMax

# third time

def maxSubArray(self, nums: List[int]) -> int:
        bestMax = -99999999999999
        currentMax = 0
        
        for i in range(len(nums)):
            currentMax = currentMax + nums[i]
            
            if currentMax > bestMax:
                bestMax = currentMax
            
            if currentMax < 0:
                currentMax = 0
        
        return bestMax

#Second time:

def maxSubArray(self, nums: List[int]) -> int:
        bestMax = -99999999999999
        currentMax = 0
        
        for i in nums:
            currentMax = currentMax + i
            
            if currentMax > bestMax:
                bestMax = currentMax
            
            if currentMax < 0:
                currentMax = 0
        
        return bestMax

#stolen solution, failed to solve 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = -999999999999
        max_ending_here = 0

        for i in range(0, len(nums)): 
            max_ending_here = max_ending_here + nums[i] 
            if (max_so_far < max_ending_here): 
                max_so_far = max_ending_here 

            if max_ending_here < 0: 
                max_ending_here = 0   
                # we reset this here because theres no benefit to continuing a sum calculation that is summing to a negative number,
                #  when we could just start at a positive. If this negative number is the current max sum,
                #  and everything else turns out negative then we'll still have this recorded as our max sum, but we clear it because if we add a positive to a negative rolling sum,
                #  its guaranteed to be worse than if we just started a new sum over, starting with a positive number. 
        return max_so_far 