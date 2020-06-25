# first try, took too long. 

class Solution:
    def maximumSwap(self, num: int) -> int:
        ns = str(num)
        nums = [int(c) for c in ns]
        
        for i in range(len(nums)):
            # if the number is not the biggest number from this point onwards
            # then there is a bigger number that could go in its place
            # our ideal (max) number is in desc order
            maxnumind = self.findMaxFromRight(nums, i)
            if nums[i] != nums[maxnumind]:
                nums[i], nums[maxnumind] = nums[maxnumind], nums[i]
                break
                
        strnums = [str(n) for n in nums ]
        return "".join(strnums)
    
    def findMaxFromRight(self, nums, lbound):
        maxnumind = len(nums)-1
        for i in range(len(nums)-1, lbound - 1, -1):
            if nums[i] > nums[maxnumind]:
                maxnumind = i
        return maxnumind