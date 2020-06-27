# second time, choppy execution 
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        
        # iterate from right to left 
        # until we find a num that isnt in desc order
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        # print(i)
        if i >= 0:
            # print("entered thing")
            # iterate from i+1 to the right until we find a val that's bigger than the one at i
            j = i+1
            nextbiggestind = i+1
            while j < len(nums) and nums[j] > nums[i]:
                j += 1
            j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # print(nums)
        # reverse everthing to the right of i
        nums[i+1:] = reversed(nums[i+1:])
        # print(nums)
        
        
        
        



#first time, ouch

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) == 1:
            return
        
        i = len(nums) - 2
        
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
            
        print("i is",i)
        
        if i >= 0:
            j = i +1
            while j < len(nums) and nums[j] > nums[i] :
                j += 1

            print("j-1 is",j-1)
        
            nums[i], nums[j-1] = nums[j-1], nums[i]
        
        j = len(nums)-1
        k = i+1 
        while k < j:
            # print("swapping ", nums[j], "and", nums[k])
            nums[j], nums[k] = nums[k], nums[j]
            j -= 1
            k += 1
        
        
        