# came up with a much more efficient way, lets see if i can remember it
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:        
        # use a counter variable which starts at the beginning of nums 
        
        
        # if the given nums list has length of 1, return that num + k
        if len(nums) == 1:
            return nums[0] + k
        
        # k -= nums[0]
        
        # iterate across nums
        i = 1
        while i < len(nums) and k > 0:
            # if the number we're looking at isnt equal to the number prior + 1
            if nums[i] != nums[i-1] + 1:
                diff = nums[i] - nums[i-1] - k
                # print(nums[i], "-", nums[i-1], "-", k, "=", diff)
                
                # if the number we're looking at - k is less than 0
                # our answer must be between this number and the previous number
                if diff < 0:
                    # subtract (current num - previous num) - 1 from k, continue
                    # print("case 1")
                    k = (diff * -1) + 1
                    # k -= (nums[i] - nums[i-1] + 1)
                    
                # if the number we're looking at - k is greater than 0
                elif diff > 0:
                    # return previous number + k
                    # print("case 2")
                    return nums[i-1] + k
                # if it is equivalent 
                elif diff == 0: 
                    # return current num - 1
                    # print("case 3")
                    # actually i think k needs to be reset to 1 ?
                    k = 1
            
            i += 1
        
        print("finished loop. k:", k)
        return nums[i-1] + k 
        
        
        



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