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