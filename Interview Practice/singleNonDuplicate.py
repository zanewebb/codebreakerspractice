# im stupid
# doesnt work
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        hi, lo, i = len(nums)-1, 0, (len(nums)-1)//2
        
        while hi > lo:
            i = (hi-lo)  // 2
            
            if nums[i-1] != nums[i] and nums[i+1] != nums[i]:
                return i
            if nums[i-1] == nums[i]:
                if ((i-1) - lo) % 2 != 0:
                    hi = i-1
                else:
                    lo = i
            if nums[i+1] == nums[i]:
                if (i - lo) % 2 != 0:
                    hi = i
                else:
                    lo = i+1
        return nums[hi]
        


# LC code
def singleNonDuplicate(self, nums: List[int]) -> int:
    lo = 0
    hi = len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if mid % 2 == 1:
            mid -= 1
        if nums[mid] == nums[mid + 1]:
            lo = mid + 2
        else:
            hi = mid
    return nums[lo]


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