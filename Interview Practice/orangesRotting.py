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