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