# so close, shouldnt have tried setting the intial rolling prod to a value other than 1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        output = [0] * len(nums)
        
        
        output[0] = 1
        
        for i in range(1,len(nums)):
            output[i] = nums[i-1] * output[i-1]
        
        rollingprod = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= rollingprod
            rollingprod *= nums[i]
        
        return output


# approved answer
# the trick is to do just two passes, one where you populate each index with the rolling profuct of everything to the left
# second pass keeps track of the rolling product from the right, multiply that into each output index and that should be it
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [0] * len(nums)
        output[0] = 1
        for i in range(1, len(nums)):
            output[i] = output[i-1]*nums[i-1]
        
        rollingprod = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * rollingprod
            rollingprod *= nums[i]
        
        return output

# PLEASE NOTE THAT THIS SOLUTION IS INVALID
# ONE REQUIREMENT OF THIS PROBLEM IS THAT IT MUST BE O(N), THIS IS O(N^2)
# MUST NOT USE DIVISION TO SOLVE THIS
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [None]*len(nums)
        
        rollingprod = 1
        for i in range(0, len(nums)):
            tempprod = 1
            for j in range(i+1, len(nums)):
                if j < len(nums):
                    tempprod *= nums[j]
            output[i] = tempprod * rollingprod
            
            rollingprod *= nums[i]
                
        
        return output