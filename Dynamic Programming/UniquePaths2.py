class Solution:

    # third time? rough time completing it
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        if len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1:
            return 1
        
            
        
        # mark obstacles
        for r in range(len(obstacleGrid)):
            for c in range(len(obstacleGrid[0])):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = -1
        # prep corner
        obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] == 1
        
        # print(obstacleGrid)
        
        # prep right side
        for r in range(len(obstacleGrid)-2, -1, -1):
            if obstacleGrid[r][len(obstacleGrid[0])-1] != -1:
                obstacleGrid[r][len(obstacleGrid[0])-1] = 1 if obstacleGrid[r+1][len(obstacleGrid[0])-1] != -1 else -1
                
        
        # prep bottom side
        for c in range(len(obstacleGrid[0])-2, -1, -1):
            if obstacleGrid[len(obstacleGrid)-1][c] != -1:
                obstacleGrid[len(obstacleGrid)-1][c] = 1 if obstacleGrid[len(obstacleGrid)-1][c+1] != -1 else -1
                
        # print(obstacleGrid)
        
        for r in range(len(obstacleGrid)-2, -1, -1):
            for c in range(len(obstacleGrid[0])-2, -1, -1):
                if obstacleGrid[r][c] != -1:
                    obstacleGrid[r][c] = (obstacleGrid[r+1][c] if obstacleGrid[r+1][c] != -1 else 0)+(obstacleGrid[r][c+1] if obstacleGrid[r][c+1] != -1 else 0)
        
        # print(obstacleGrid)
        return obstacleGrid[0][0]



        

   # after following the accepted solution this is much nicer
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            obstacleGrid[0][0] = 1
        
        # set the top and leftmost rows
        for i in range(1,len(obstacleGrid)):
            obstacleGrid[i][0] = 0 if obstacleGrid[i][0] == 1 else obstacleGrid[i-1][0] 
        for i in range(1,len(obstacleGrid[0])):
            obstacleGrid[0][i] = 0 if obstacleGrid[0][i] == 1 else obstacleGrid[0][i-1]
    
        
        for r in range(1,len(obstacleGrid)):
            for c in range(1,len(obstacleGrid[0])):
                obstacleGrid[r][c] = obstacleGrid[r-1][c] + obstacleGrid[r][c-1] if obstacleGrid[r][c] != 1 else 0
        
                
        return obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]

   # first time, super sloppy execution but 77% time 
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] == 1:
            return 0
        
        # initial position is 0, 0
        
        # build out solution grid starting from destination
        
        # clean the obstacles so that they now are "X"
        # print(obstacleGrid)
        for r in range(len(obstacleGrid)):
            for c in range(len(obstacleGrid[0])):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = "X"
        
        # start by putting ones on the right and bottom edges
        obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] = 1
        for i in range(len(obstacleGrid)-2, -1, -1):
            if obstacleGrid[i][len(obstacleGrid[0])-1] != "X" and obstacleGrid[i+1][len(obstacleGrid[0])-1] == 1:
                obstacleGrid[i][len(obstacleGrid[0])-1] = 1
            else:
                obstacleGrid[i][len(obstacleGrid[0])-1] = 0
        
        for i in range(len(obstacleGrid[0])-2, -1, -1):
            if obstacleGrid[len(obstacleGrid)-1][i] != "X" and obstacleGrid[len(obstacleGrid)-1][i+1] == 1:
                obstacleGrid[len(obstacleGrid)-1][i] = 1
            else:
                obstacleGrid[len(obstacleGrid)-1][i] = 0
        
        # fill out the rest of the grid following the rule that
        # grid[r][c] = grid[r+1][c] + grid[r][c+1]
        for r in range(len(obstacleGrid)-2, -1,-1):
            for c in range(len(obstacleGrid[0])-2,-1, -1):
                if obstacleGrid[r][c] != "X":
                    down = obstacleGrid[r+1][c] if obstacleGrid[r+1][c] != "X" else 0
                    right = obstacleGrid[r][c+1] if obstacleGrid[r][c+1] != "X" else 0
                    obstacleGrid[r][c] =  down + right
                
        # print(obstacleGrid)
        
        # select the value at the start index (0,0)
        return obstacleGrid[0][0]