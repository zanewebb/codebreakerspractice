# longestMountainInArray.py

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        # if length is less than three then there can be no mountain
        if len(A) < 3:
            return 0
        
        # track maxDist, peakHeight and direction (up the mountain or down) 
        maxDist = direction = 0
        curDist = 1
        
        # as you iterate across the values, starting at index 0
        for i in range(1,len(A)):
            # reset case
            # if your current value is greater than the one before it and the direction is -1
            if (A[i] >= A[i-1] and direction == -1) or (A[i] == A[i-1] and direction == 1):
                # set current distance back to 0
                curDist = 1
                # set direction to 0
                direction = 0
            
            # if your current value is greater than the one before it 
            if A[i] > A[i-1]: 
                # increment current distance
                curDist += 1
                direction = 1
                
            
            #  else if your current value is less than the one before it
            #  value following peak cannot be equal to peak, mesas arent mountains
            if A[i] < A[i-1] and direction != 0:
                # set direction to -1
                direction = -1
                # increment current distance
                curDist += 1
                # if the current distance is greater than max distance, update max distance
                if curDist > maxDist:
                    maxDist = curDist
        
        return maxDist if maxDist >= 3 else 0