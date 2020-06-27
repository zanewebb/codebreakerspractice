
# abnormally slow execution, test cases must be huge. 
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        counter = nums[0] 
        nums = deque(nums)
        while k > 0 and len(nums) > 0:
            nextnum = nums.popleft()
            while nextnum > counter + 1 and k > 0:
                counter += 1
                k -= 1
            if k > 0 :
                counter = nextnum
        
        return counter + k
    
    
    
    
    '''
    [4,7,9,10]
    3
    
    4
    4
    3
    
    7
    4 5 6
    3 2 1
    
    9
    6 7
    1 0
    
    '''