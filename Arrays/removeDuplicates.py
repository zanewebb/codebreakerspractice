# removeDuplicates.py

#fourth or fifth time
def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0 if len(nums) == 0 else 1
        
        # track uniqueNumsLength and an iterator
        uniqueLen = 1
        # iterate over nums from 1, len(nums) -1 
        for i in range(1,len(nums)):
            # if the number in question is different than the one before it,
            if nums[i] != nums[i-1]: 
                # assign its value to the position at uniqueNumsLength
                nums[uniqueLen] = nums[i]
                # iterate uniqueNumsLength
                uniqueLen += 1
        
        return uniqueLen

# third time, wavered for a second but got it

def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        
        j = 0
        for i in range(1,len(nums)):
            # print("i: ", i)
            # print("j: ", j)
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
            # print(nums)
        
        return j+1

# second time, schmancy solution

def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        
        # pointer of the most recently updated index
        i = 0
        
        # each time we encounter a unique value, assign that value to index i
        for x in range(1,len(nums)):
            if nums[x] != nums[i]:
                nums[i+1] = nums[x]
                i += 1
        
        # return the index + 1 as the length
        return i +1


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