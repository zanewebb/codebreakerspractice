# second time, remembered / reconstructed my solution
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # this is a dict of 
        # rollingsum : first seen index
        rollingsums = {0:-1}
        rollingsum = 0
        maxlen = 0
        
        for i,n in enumerate(nums):
            val = 1 if n == 1 else -1
            rollingsum = val + rollingsum
            
            if rollingsum in rollingsums:
                maxlen = max(i-rollingsums[rollingsum], maxlen)
            else:
                rollingsums[rollingsum] = i
                
        return maxlen   
        # 0   0   1   0   1   0   1   1   0   1 
        # -1  -2  -1  -2  -1  -2  -1  0  -1   0
        
        
        # [ 0, 1, 0 ]
        # [-1, 0, -1]
        # { 0: -1, -1: 0,  }

# first time, wiped out
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxLength = 0
        seen = {0:-1}
        rolling = 0

        for i, n in enumerate(nums):
            rolling += 1 if n == 1 else -1
            if rolling not in seen:
                seen[rolling] = i
            else:
                maxLength = max(maxLength, i - seen[rolling])

        return maxLength