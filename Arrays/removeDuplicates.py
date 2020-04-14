# removeDuplicates.py

#got it first try wow

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointer/sliding window approach
        left = right = 0
        
        # two pointers that move along, one ahead of the other
        while left < len(nums)-1 and right+1 <= len(nums)-1:
            right += 1
            # as long as they both point to the same value, pop the second index
            while right <= len(nums)-1 and nums[right] == nums[left]:
                nums.pop(right)
            
            left +=1
        
        # return length
        return len(nums)