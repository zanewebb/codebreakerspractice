#sortArray.py

class Solution:


   # first time, solution works, merge sort is space intensive so, leetcode's dumbass 100000000000000000000000000000000000000 value test case exceeded time but all others worked fine
    def sortArray(self, nums: List[int]) -> List[int]:
        #merge sort attempt
        self.mergeSort(nums, 0 , len(nums)-1 )
        return nums
    
    def mergeSort(self, nums: List[int], lo:int, hi:int):
        # if we're only dealing with one index, nothing to do
        if lo >= hi:
            return
        
        # merge sort the lower half
        self.mergeSort(nums, lo, (hi+lo)//2 )
        # merge sort the upper half
        self.mergeSort(nums, (hi+lo)//2 + 1, hi)
        # merge the sorted halves
        self.merge(nums, lo, (hi+lo)//2 + 1, hi)
        
    
    
    def merge(self, nums: List[int], lo1:int, lo2:int, hi:int):
        # declare a copy of the nums array, a pointer for the nums array, and two pointers for the copy
        dup = nums[:]
        cur = lo1
        dup1 = lo1
        dup2 = lo2
        
        # while nums pointer is less than or equal to the high index
        while cur <= hi:
            # if the values at both copy pointers are valid, eval them against each other and increment the winner
            if dup1 < lo2 and dup2 <= hi:
                if dup[dup1] < dup[dup2]:
                    nums[cur] = dup[dup1]
                    dup1 += 1
                else:
                    nums[cur] = dup[dup2]
                    dup2 += 1
            # if only one value at one pointer is within its range, then place that at the nums pointer index
            elif dup1 < lo2:
                nums[cur] = dup[dup1]
                dup1 += 1
            else:
                nums[cur] = dup[dup2]
                dup2 += 1
 
            cur += 1
        
        
    