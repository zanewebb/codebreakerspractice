#maxSubArray


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