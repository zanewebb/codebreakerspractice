# third time
# remembered it
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # hold dict of rolling sum : occurences of this sum
        occs = {0:1}
        count = 0
        rollingSum = 0
        
        # build a list of length len(nums) that has the rolling sum of the nums
        for n in nums:
            rollingSum += n
            # at any point, if the rolling sum - k is in the dict then we add the # of occurences to our count 
            if rollingSum - k in occs:
                count += occs[rollingSum-k]
            occs[rollingSum] = occs.get(rollingSum,0) + 1
        
        return count

# second time, ouch, complete wipeout

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # one pass, dict for rolling sum occurences
        
        sums = {0:1}
        rollingSum = count = 0
        
        for n in nums:
            rollingSum += n
            if rollingSum - k in sums:
                count += sums[rollingSum - k]
            sums[rollingSum] = sums.get(rollingSum, 0) + 1
        
        return count



class Solution:


   # doesnt work
   
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 1 and k != nums[0]:
            return 0
        
        rollingSum = 0
        sums = {0:1}
        ansCount = 0
        for num in nums:
            rollingSum += num
            if rollingSum in sums:
                sums[rollingSum] += 1
            else:
                sums[rollingSum] = 1
            if rollingSum - k in sums:
                ansCount += sums[rollingSum-k]
        
        return ansCount