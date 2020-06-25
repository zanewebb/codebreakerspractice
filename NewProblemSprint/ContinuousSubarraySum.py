#efficient solution, found on forums
# similar to another problem ive done, dont remember the name
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        
        rollingsum = 0
        seen = {0:-1}
        for i, n in enumerate(nums):
            rollingsum += n 
            # need to double check that k is not 0, cant mod that
            key = rollingsum % k if k != 0 else rollingsum
            
            if key in seen and i - seen[key] > 1:
                return True
            elif key not in seen:
                seen[key] = i
        
        return False
        

# first try, TLE :(

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        # [23, 2, 4, 6, 7]   k=6
        #  23  2  6
        #      l  r
        
        if len(nums) < 2 or (k == 0 and 0 not in nums):
            return False
        
        # if k == 0 and 0 in nums:
        #     return True
        
        l, r = 0, 0
        rollingSum = 0
        
        # trying to memoize. str rep of l and r,
        tried = set()
        found = self.look(0, len(nums), k, nums, tried)
        print("found is", found)
        return found
        
        
    def look(self, l, r, k, nums, tried):
        # check if this l and r combo has already been tried, if so, return
        # also check if we're alreday done (given in the done bool)
        key = str(l)+"-"+str(r)
        if key in tried or l == r or r-l < 2:
            return False
        
        
        # check if the given sub array is a multiple of the target
        if (k == 0 and sum(nums[l:r]) == 0) or (k != 0 and sum(nums[l:r]) % k == 0):
            print("found solution")
            return True
        else:
            # if not, add this l and r combo to the set
            tried.add(key)
            
            # try again with one more on l and one less on r
            return self.look(l+1, r, k, nums, tried) or self.look(l, r-1, k, nums, tried)
        
        
        
        