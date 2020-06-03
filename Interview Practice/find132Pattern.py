# fifth time
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        icandidates = [nums[0]]
        
        for i in range(1, len(nums)):
            icandidates.append(min(nums[i], icandidates[i-1]))
            
        kcandidates = []
        jcandidates = nums
        
        for ind in range(len(jcandidates)-1, -1, -1):
            if jcandidates[ind] > icandidates[ind]:
                while len(kcandidates) > 0 and kcandidates[-1] <= icandidates[ind]:
                    kcandidates.pop()
                if len(kcandidates) > 0 and kcandidates[-1] < jcandidates[ind]:
                    return True
                kcandidates.append(jcandidates[ind])
        return False



# didnt have to look at the solution, typed the justification for each line
# fourth time

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        # populate our list of 
        # "best i candidate at each index"
        iCandidates = [nums[0]]
        for i in range(1, len(nums)):
            iCandidates.append(min(iCandidates[i-1], nums[i])) 
        
        # doing this for my own clarity
        jCandidates = nums
        
        # declare a "Stack" to store our valid k options at the current index
        kCandidates = []
        
        # traverse backwards down our J candidates
        for ind in range(len(jCandidates)-1, -1, -1):
            # we first need to verify that the j candidate is valid at the very least
            # if the j candidate isnt valid then there is no way that it could be a k candidate
            if iCandidates[ind] < jCandidates[ind]:
                
                # now that we know that is valid
                # lets exclude k candidates that do not work with this i candidate
                while len(kCandidates) > 0 and kCandidates[-1] <= iCandidates[ind]:
                    kCandidates.pop()
                
                # if there is anything left in our stack of k candidates
                # and that candidate is valid, we've satisfied all conditions
                if len(kCandidates) > 0 and kCandidates[-1] < jCandidates[ind]:
                    return True
                
                # if it wasnt a hit on the 132 pattern, that means we've hit the case where
                # j was valid relative to i
                # k was valid relative to i OR THERE ARE NO MORE K's
                # EITHER k was not valid relative to j OR there was no K left that met the previous conditions
                kCandidates.append(jCandidates[ind])
        
        return False
            



# this is extremely hard for me to comprehend
# third time
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        # create list smallest value encountered so far, left to right (1's)
        mins = [nums[0]]
        i = 1
        while i < len(nums):
            mins.append(min(mins[i-1], nums[i]))
            i += 1
        
        # traverse backwards down the i list and nums list 
        k = []
        i = j = len(nums)-1
        while i >= 0 and j >= 0:
            if mins[i] < nums[j]:
                while len(k) > 0 and k[-1] <= mins[i]:
                    k.pop()
                if len(k) > 0 and k[-1] < nums[j]:
                    return True
                k.append(nums[j])
            i -= 1
            j -= 1
        return False 



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