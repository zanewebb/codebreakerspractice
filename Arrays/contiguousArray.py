

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