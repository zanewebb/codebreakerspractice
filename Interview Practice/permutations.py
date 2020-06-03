# third time

class Solution:
    
    def __init__(self):
        self.nums = None
        self.ans = []
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.look(0)
        return self.ans
        
    def look(self, ind):
        if ind >= len(self.nums):
            self.ans.append(self.nums[:])
            return
        
        # [1, 2, 3]
        
        for i in range(ind, len(self.nums)):
            self.nums[i], self.nums[ind] = self.nums[ind], self.nums[i]
            self.look(ind + 1)
            self.nums[i], self.nums[ind] = self.nums[ind], self.nums[i]
            


# second time

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.permutee(nums, ans, 0)
        return ans
    def permutee(self, nums, ans, ind):
        # if this round of permutations has reached the end of the nums list
        if ind == len(nums):
            # append a deep copy
            ans.append(nums[:])
            
        
        for i in range(ind, len(nums)):
            nums[i], nums[ind] = nums[ind], nums[i]          
            self.permutee(nums, ans, ind+1)
            nums[i], nums[ind] = nums[ind], nums[i] 



class Solution:
    def __init__(self):
        self.nums = None
        self.ans = []
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.backtrack(0)
        return self.ans
        
    def backtrack(self, ind):
        # if the given index is out of bounds append the current state of the array to the ans
        if ind == len(self.nums):
            self.ans.append(self.nums[:])
            
        # iterate over the remaining indicies (from ind to the end)
        for i in range(ind,len(self.nums)):
            # swap the index of the iterator with the given index
            self.nums[ind], self.nums[i] = self.nums[i], self.nums[ind]
            # recursively call backtrack with the given ind + 1
            self.backtrack(ind + 1)
            # swap the index of the iterator BACK with the given index
            # this is so that we are able to continue exploring the state of the other branches of perms
            self.nums[ind], self.nums[i] = self.nums[i], self.nums[ind]