
class Solution:

   #second time, one of the accepted solutions 
   
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        
        # stablish list of possible i's
        mins = [nums[0]]
        i = 1
        while i < len(nums):
            mins.append(min(mins[i-1], nums[i]))
            i += 1
        
        # create stack to store potential k's
        ks = []
        
        # iterate over nums in search for a j that is valid
        for j in range(len(nums)-1, -1, -1):
            # if this number is a valid j candidate
            if nums[j] > mins[j]:
                # shed k candidates that would not meet this j's associated i candidate
                while len(ks) > 0 and ks[-1] <= mins[j]:
                    ks.pop()
                
                # if we didnt shed everything, verify that the most recently checked k candidate is valid
                if len(ks) > 0 and ks[-1] < nums[j]:
                    return True
                
                # if there wasnt a valid set, add this as a potential future k
                ks.append(nums[j])
        
        return False


# couldnt solve it

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        # three pointer approach
        i, j, k = 0, 1, len(nums)-1
        
        def checkValid(i,j,k,nums):
            if nums[i] < nums[k] and nums[j] > nums[k] and i < j and j < k:
                return True
            else:
                return False
        
        # going to try attaching indicies and sorting
        # nums = sorted(list(enumerate(nums)), key= lambda x: x[1])
        # print(nums)
        
        # while 3 indicies are being considered
        while i < len(nums)-2:
            j = i+1
            k = len(nums)-1 
            print(i,j,k)
            while nums[k] <= nums[i] and j < k:
                k -= 1
                
            # wasn't able to find a value nums[k] that was greater than nums[i]
            if j == k:
                i += 1
                continue
                
            if checkValid(i,j,k,nums):
                return True
            
            while nums[j] <= nums[k] and j < k:
                j += 1
                
            # wasn't able to find a value nums[j] that was greater than nums[k]
            if j == k:
                i += 1
                continue
            
            return True
#             if checkValid(i,j,k,nums):
#                 return True
            
#             i += 1
            
        return False