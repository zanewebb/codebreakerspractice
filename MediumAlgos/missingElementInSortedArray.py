
# much smarter
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # Return how many numbers are missing until nums[idx]
        missing = lambda idx: nums[idx] - nums[0] - idx
            
        n = len(nums)
        # If kth missing number is larger than 
        # the last element of the array
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1) 
        
        left, right = 0, n - 1
        # find left = right index such that 
        # missing(left - 1) < k <= missing(left)
        while left != right:
            pivot = left + (right - left) // 2
            
            if missing(pivot) < k:
                left = pivot + 1
            else:
                right = pivot 
        
        # kth missing number is greater than nums[left - 1]
        # and less than nums[left]
        return nums[left - 1] + k - missing(left - 1) 


# REAlly slow and inefficient but it worked?
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if i < len(nums)-1:
                count = nums[i]
                for n in range(nums[i]+1,nums[i+1]):
                    count += 1
                    k -= 1
                    # print(count, k)
                    if k == 0:
                        return count
            else:
                return nums[i] + k