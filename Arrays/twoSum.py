# sixth time, dict way is more space but faster over all ?

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(enumerate(nums), key=lambda x: x[1])
        
        l, r = 0, len(nums)-1
        
        while l < r:
            if nums[l][1] + nums[r][1] == target:
                return [nums[l][0],nums[r][0]]
            elif nums[l][1] + nums[r][1] < target:
                l += 1
            else:
                r -= 1

# twoSum.py
class Solution:


    # fifth time
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # store dict
        comps = {}
        
        # for each num, enumerated
        for i, n in enumerate(nums):
            # find the compliment (?) of this number to the target
            comp = target - n
            
            # if that compliment is not in the dict, then add it with the index of this num
            if comp not in comps:
                comps[n] = i
            
            # if it IS in the dict, we found its other number, so return the index at 
            # the compliment key and the current index
            else:
                return [comps[comp], i]

#fourth time 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(list(enumerate(nums)), key=lambda x: x[1])
        print(nums)
        l , r = 0, len(nums)-1
        
        while nums[l][1] + nums[r][1] != target:
            if nums[l][1] + nums[r][1] < target:
                l += 1
            elif nums[l][1] + nums[r][1] > target:
                r -= 1
        
        return [nums[l][0],nums[r][0]]

# third time SORTING WITH LAMBDA IS MUCH SLOWER

def twoSum(self, nums: List[int], target: int) -> List[int]:
        # solution requirements guarantee that we have at least 2 indicies in input array
        
        # iterate over sorted enumerated values
        nums = list(sorted(enumerate(nums), key= lambda a: a[1])) 
        
        
        # two pointer method, left and right
        l, r = 0, len(nums)-1
        while l < r:
            if nums[l][1] + nums[r][1] < target:
                l += 1
            if nums[l][1] + nums[r][1] > target:
                r -= 1
            if nums[l][1] + nums[r][1] == target:
                return [nums[l][0], nums[r][0]]
        


   # second try:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
         # solution requirements guarantee that we have at least 2 indicies in input array
         
         # zip the nums with indicies
         nums = sorted(list(zip(nums, range(len(nums)))))
         
         # left and right pointers to find the target
         left = 0
         right = len(nums)-1
         while nums[left][0] + nums[right][0] != target:
               if nums[left][0] + nums[right][0] > target:
                  right -= 1
                  
               if nums[left][0] + nums[right][0] < target:
                  left += 1
         
         return [nums[left][1] , nums[right][1]]


   #first try woo
   def twoSum(self, nums: List[int], target: int) -> List[int]:
      # solution requirements guarantee that we have at least 2 indicies in input array        
      
      # zip input array with some index nums
      nums = list(zip(nums, range(len(nums))))
      # sort input array
      nums = sorted(nums, key=lambda x: x[0])
      
      # two pointers, left and right
      left = 0
      right = len(nums)-1
      
      while nums[left][0] + nums[right][0] != target:
         # if sum of two vals at pointers is too high, move right inwards
         if nums[left][0] + nums[right][0] > target:
               right -= 1
         
         # if sum of two vals at pointers is too low, move left inwards
         if nums[left][0] + nums[right][0] < target:
               left += 1
               
      # return solution indicies 
      return [nums[left][1],nums[right][1]]