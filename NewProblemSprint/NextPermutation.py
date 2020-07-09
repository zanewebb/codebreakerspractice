# still trouble with some edge cases. MAKE SURE J STARTS AT i + 1
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        
        i = len(nums) - 2
        
        # iterate right until we find a num that doesnt match the pattern of always increasing
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        print(i)
        
        # if we didnt hit the front of nums, iterate right until we find an index lesser than i
        if i >= 0:
            j = i+1
            while j < len(nums) and nums[i] < nums[j]:
                j += 1
            print(j)
            # swap those two indexes
            nums[i], nums[j-1] = nums[j-1], nums[i]
            
        # reverse everything from i+1 to the end
        nums[i + 1:] = reversed(nums[i+1:])
        
        return
        
        
        
        
        
        
        
        
        
        


# tricky to catch all the edge cases but finally got it
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) < 2:
            return
        
        i = len(nums)-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        print(i)
        
        # if we arent just reversing the whole thing
        if i >= 0 :
            j = i + 1 
            while j < len(nums) and nums[j] > nums[i]:
                # 3 2 5 4 1
                #   i     
                
                # 1 2 5 4 3 
                
                j += 1
            
            print(j)
            
            # if j < len(nums):
            nums[i], nums[j-1] = nums[j-1], nums[i]
            # else:
            #     nums[i], nums[-1] = nums[-1], nums[i]
            
        nums[i+1:] = reversed(nums[i+1:])
        

# holy moly im dumb, completely fell apart on execution again
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) == 1:
            return
        
        i = len(nums)-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        print(i)
        
        if i >= 0:
            j = i+1
            while j < len(nums) and nums[j] > nums[i]:
                j += 1
            j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            print(nums)
        
        nums[i+1:] = reversed(nums[i+1:])


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
        
        
        