# twoSum.py

#first try woo
class Solution:
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