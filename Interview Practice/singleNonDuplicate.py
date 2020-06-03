# accepted solution, binary search using "which half has an odd number of indexes" as the target
def singleNonDuplicate(self, nums: List[int]) -> int:
    lo = 0
    hi = len(nums) - 1   
    while lo < hi:
        mid = lo + (hi - lo) // 2
        halves_are_even = (hi - mid) % 2 == 0
        if nums[mid + 1] == nums[mid]:
            if halves_are_even:
                lo = mid + 2
            else:
                hi = mid - 1
        elif nums[mid - 1] == nums[mid]:
            if halves_are_even:
                hi = mid - 2
            else:
                lo = mid + 1
        else:
            return nums[mid]
    return nums[lo]



# works, brute force though, first try
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        i = 1
        
        while i < len(nums):
            if nums[i-1] != nums[i]:
                return nums[i-1]
            else:
                i += 2
        
        if nums[-1] != nums[-2]:
            return nums[-1]