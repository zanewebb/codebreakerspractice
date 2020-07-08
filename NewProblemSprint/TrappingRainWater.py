# I forgot it but i came up with a working solution from what i did remember
class Solution:
    def trap(self, height: List[int]) -> int:
        
        fromleftmaxes = [-1] * len(height)
        fromrightmaxes = [-1] * len(height)
        
        # get maxes from the left side 
        curmax = -1
        for i in range(len(height)):
            curmax = max(curmax, height[i])
            fromleftmaxes[i] = curmax
        
        # do the same from the right
        curmax = -1
        for i in range(len(height)-1, -1, -1):
            curmax = max(curmax, height[i])
            fromrightmaxes[i] = curmax
        
        # iterate over the maxes and choose the lesser max for the water calculation
        water = 0
        for i in range(len(height)):
            water += min(fromleftmaxes[i],fromrightmaxes[i]) - height[i]
        
        
        return water
            
            
            


# smart way to do it
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        l,r = 0, len(height)-1
        
        leftmax = 0
        rightmax = 0
        water = 0
        
        while l < r:
            if height[l] < height[r]:
                leftmax = max(leftmax, height[l])
                water += leftmax - height[l]
                l += 1
            else:
                rightmax = max(rightmax, height[r])
                water += rightmax - height[r]
                r -= 1
                
            
        return water
        
        
        

# close but couldnt get it, need to account for land better? probably doable in one pass
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        localmaxima = []
        curmax = height[0]
        curmaxloc = 0
        for i in range(1,len(height)):
            if height[i] > height[i-1]:
                curmax, curmaxloc = max(curmax, height[i]), i
            elif height[i] < height[i-1] and curmax > 0:
                localmaxima.append((curmax,curmaxloc))
                curmax = 0
        
        if curmax > 0:
                localmaxima.append((curmax,curmaxloc))
                curmax = 0
        print(localmaxima)
                
        if len(localmaxima) <= 1:
            return 0
        
        water = 0
        for i in range(1, len(localmaxima)):
            # print(localmaxima[i-1], localmaxima[i])
            h = min(localmaxima[i][0], localmaxima[i-1][0])
            tempwater = h * (localmaxima[i][1] - localmaxima[i-1][1]-1) 
            
            land = 0
            for j in range(localmaxima[i-1][1]+1, localmaxima[i][1]):
                if height[j] < h:
                    land += height[j]
            print(tempwater,land)
            
            # land = sum(height[localmaxima[i-1][1]+1:localmaxima[i][1]])
            # print(tempwater, land)
            water += tempwater - land
            
        return water
        
        
        