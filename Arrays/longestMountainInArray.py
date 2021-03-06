# longestMountainInArray.py


                


class Solution:

# fifth time
def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        
        # if the length is less than 3, cant be a mountain at all
        direction = maxLen = 0
        curLen = 1
        
        # for each num
        i = 1
        while i < len(A):
            # if the height is higher than the last
            if A[i] > A[i-1]:
                # if the direction is currently down, set the curLen to 1
                if direction == -1:
                    curLen = 1
                # set the direction to up, increment curlen
                direction, curLen = 1, curLen + 1
                
            # elif the height is lower than the last and the curlen is >= 2
            elif A[i] < A[i-1] and curLen >= 2:
                # increment curLen, set the direction to down
                direction, curLen = -1, curLen + 1
                
                # set maxLen to max of curLen and itself
                maxLen = max(curLen, maxLen)
                
            # else (height must be equal to the last)
            else:
                #set curLen and direction to 0
                curLen, direction = 1, 0
            
            i += 1
        
        return maxLen

# fourth solution

def longestMountain(self, A: List[int]) -> int:
        # if the length is less than 3, cant be a mountain at all
        if len(A) < 3:
            return 0
        direction, bestSize, curSize = 0, 1, 1
        
        for i in range(1,len(A)):
            if A[i] < A[i-1] and direction != 0:
                direction = -1
                curSize += 1
                
                bestSize = max(curSize, bestSize)
                
            
            elif A[i] > A[i-1]:
                if direction == -1:
                    curSize = 1
                
                direction = 1
                curSize += 1
                
            else:
                direction = 0
                curSize = 1
        
        if bestSize >=3:
            return bestSize
        
        else: 
            return 0



# third time, marginally cleaner. 96% time, 100% space

def longestMountain(self, A: List[int]) -> int:
        # if the length is less than 3, cant be a mountain at all
        if len(A) < 3:
            return 0
        
        # track direction, best dist and current dist
        direction, bestDist, curDist = 0, 0 , 1 
        
        # iterate over A
        for i,h in enumerate(A):
            if i > 0:
                # if the current val is greater than its previous
                if A[i-1] < h:
                    # if we were going down and now we're going up, reset the values
                    if direction == -1: 
                        # reset the current distance to 1, set the direciton to 1
                        curDist, direction = 2, 1
                    else:
                        # increment current distance, set direction to 1
                        curDist, direction = curDist + 1, 1
                    
                # if the current val is less than its previous, and the direction isnt 0
                if A[i-1] > h and direction != 0: 
                     # increment current distance, set direction to 1
                    curDist, direction = curDist + 1, -1 
                    
                    # check if current dist is greater than best dist 
                    if curDist > bestDist:
                        # update if so
                        bestDist = curDist
                            
                # if the current val is the same as the previous
                if A[i-1] == h:
                    # set the current dist to 1, set the direction to 0
                    curDist, direction = 1, 0
            
            # print(i, h)
            # print(curDist, bestDist, direction)
        
        return bestDist


        

# second time, incomplete answer. Direction indicator approach works fine
def longestMountain(self, A: List[int]) -> int:
        # if length is less than three then there can be no mountain
        if len(A) < 3:
            return = 0
        
        maxDist = curDist = 1
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                if
                curDist += 1
            
            if A[i] < A[i-1] and curDist > 1:
                curDist += 1
                
            if curDist > maxDist:
                maxDist = curDist

#first time, solved it
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