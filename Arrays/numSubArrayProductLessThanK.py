# numSubArrayProductLessThanK.py

# second time: solved it almost, for some reason using len(nums[l:r]) + 1 doesnt fly, but left - right + 1 does ?

def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        
        # track l and r of window, both at 0 intially
        # windowProduct that starts at 1 and count of sub arrays
        l, r, count, windowProduct = 0, 0, 0, 1
        
        # while r < len(nums)
        while r < len(nums):
            # windowProduct *= nums[r]
            windowProduct *= nums[r]
            
            # while windowProduct is > k
            while windowProduct >= k :
                # divide window product by nums[l]
                windowProduct /= nums[l]
                
                # increment l
                l += 1
            
            count += r - l + 1
                
            # print(l, r, count, windowProduct)
            # increment r
            r += 1
        
        return count

# accepted solution
def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans


# first try, read the problem wrong like an idiot and thought it was sum. Got killed by some edge cases with K being zero, ran way over time :(
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # almost certain this is a sliding window solution
        # keyword in the problem being "contiguous"
        
        count = 0
        
        # because our domain of values is only positive or 0, we know that 
        # once the window has exceeded the value K, we can reel back in the start of the window range
        
        # tracking s and e (start and end of window) and the sum
        s, e, windowProduct = 0, 0, nums[0]
        # while the window has not traversed the entire array
        while s < len(nums)-1:            
            # if the sum of the window is less than k
            if windowProduct < k and e < len(nums):
                # increment the count
                print("adding to count: ", len(nums[s:e])+1)
                count += len(nums[s:e])+1
                
                # if the e is within bounds then increment the e
                if e < len(nums)-1:
                    # extend the window
                    e += 1

                    # update the product
                    windowProduct *= nums[e]
                else:
                    while s<e:
                        # close the window
                        s += 1

                        # update the product
                        windowProduct /= nums[s]
               
            
            # elif the sum of the window is greater than or equal to k
            elif windowProduct >= k:
                while windowProduct >= k and s < e:
                    # divide the value of nums[s] out of product
                    windowProduct /= nums[s]

                    # increment s to close the window
                    s += 1
            else:
                s += 1
        
        return count