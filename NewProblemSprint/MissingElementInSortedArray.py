
# second time
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        count = nums[0]
        i = 0
        while i < len(nums) and k > 0:
            if nums[i] > count + 1:
                while count+1 < nums[i] and k > 0:
                    count += 1
                    k -= 1
            if k > 0:
                count = nums[i]
                
            i += 1
        
        return count + k
            


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