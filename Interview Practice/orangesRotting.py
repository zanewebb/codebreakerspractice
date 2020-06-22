
# third time

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # iterate over and record which oranges are currently rotting
        rotting = []
        freshCount = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotting.append([r,c])
                elif grid[r][c] == 1:
                    freshCount += 1
        
        # loop until we have no longer rotted any new oranges
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        minutes = 0
        while True:
            #print(rotting)
            newRotting = []
            for ro in rotting:
                # each loop attempt to rot in all directions
                for d in directions:
                    # if rotting was successful then record that location as a new rotting orange
                    r = ro[0] + d[0]
                    c = ro[1] + d[1]
                    if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]) and grid[r][c] == 1:
                        grid[r][c] = 2
                        freshCount -= 1
                        newRotting.append([r,c])

            rotting = newRotting
            if len(rotting) == 0 and freshCount == 0:
                return minutes
            elif len(rotting) == 0 and freshCount != 0:
                return -1
            else:
                minutes += 1

# second time
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # figure out what's currently rotting
        rotting = []
        totalOranges = 0
        totalRotted = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotting.append([r,c])
                    totalOranges += 1
                    totalRotted += 1
                elif grid[r][c] == 1:
                    totalOranges += 1
        
        # track the count, and new rotting oranges
        minutes = 0
        newRotting = []
        directions = [[0,1], [0,-1], [1,0], [-1,0]] # right, left, down, up
        while True:
            for ro in rotting:
                for d in directions:
                    r = ro[0] + d[0]
                    c = ro[1] + d[1]
                    if 0 <= r < len(grid) and  0 <= c < len(grid[0]) and grid[r][c] == 1:
                        # track the new rotting orange
                        newRotting.append([r,c])
                        
                        # set that orange to be rotting
                        grid[r][c] = 2
                        
                        # increment our rotted count
                        totalRotted += 1
                        
            # if we rotted no new oranges, then the previous minute was the last minute
            if len(newRotting) == 0 :
                if totalRotted == totalOranges:
                    return minutes
                else:
                    return -1
            
            rotting = newRotting
            newRotting = []
            minutes += 1

# First try after reviewing solution

#this section
        rotting = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    rotting.append([i,j])

# can be shortened to this
   rotting = [[i,j] for i in range(grid) for j in range(grid[i]) if grid[i][j] == 1]

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # identify the positions of all rotting oranges
        rotting = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    rotting.append([i,j])
        
        # declare the directions that a rotting orange could affect
        directions = [[1,0],[-1,0],[0,1],[0,-1]] 
        minutes = 0
        # loop over each "minute" or round of rotting
        while True:
            newRotting = []
            # for each wave of rotting, attempt to rot in all directions of new rotting oranges
            for o in rotting:
                for d in directions:
                    yo, xo = d[0] + o[0], d[1] + o[1]
                    # if a new rotting orange was identified, track that for the next round of rotting
                    if 0 <= yo < len(grid) and 0 <= xo < len(grid[0]) and grid[yo][xo] == 1:
                        newRotting.append([yo,xo]) # track it
                        grid[yo][xo] = 2 # rot it
            
            #print(newRotting)
            
            # as soon as there are no new infections, we have infected everything we can so 
            if len(newRotting) == 0:
                # we must verify if we have infected everything
                for i in range(len(grid)):
                    for j in range(len(grid[i])):
                        # if there are any oranges with a 1 instead of a 0 or a 2, it must have been unreachable
                        if grid[i][j] == 1:
                            return -1
                return minutes
            
            rotting = newRotting
            minutes += 1