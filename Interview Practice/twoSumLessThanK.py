
# extremely similar to twosum
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        # two pointer approach 
        
        # sort first
        A = sorted(A)
        
        # two pointers and max val
        i, j, maxVal = 0, len(A)-1, -1
        
        while i < j:
            curSum = A[i] + A[j]
            # move higher one in if exceeding
            if curSum >= K:
                j -= 1
                
            # else move left one in
            else:
                i += 1
            
            # if the num is under K, and bigger than our max, overwrite
            if curSum < K:
                maxVal = max(curSum, maxVal)
                
        
        return maxVal