# fourth time
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        bestDist = 0
        curDist = 0
        
        for i in range(len(nums)):
            curDist = nums[i] + i
            if i > bestDist:
                return False
            bestDist = max(curDist, bestDist)
        
        return True

# third time
def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        curMax = bestMax = 0
        
        for i, n in enumerate(nums):       
            if bestMax < i:
                return False
            bestMax = max(n + i, bestMax)
        
            
        return True

# second time

def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        maxDist = nums[0]
        ind = 0
        
        for i in nums:
            if maxDist >= len(nums)-1:
                return True
            maxDist = ind + i if ind + i > maxDist else maxDist
            ind += 1
            if ind > maxDist:
                return False
        
        return False



#first time

def canJump(self, nums: List[int]) -> bool:
        farthestInd = 0
        for i in range(len(nums)):
            if i == len(nums):
                return True
            if i > farthestInd:
                return False
            farthestInd = max(farthestInd, i + nums[i])
        
        return True