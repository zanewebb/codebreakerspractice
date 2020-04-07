def canJump(self, nums: List[int]) -> bool:
        farthestInd = 0
        for i in range(len(nums)):
            if i == len(nums):
                return True
            if i > farthestInd:
                return False
            farthestInd = max(farthestInd, i + nums[i])
        
        return True