class Solution:   


   # was able to implement after watching the teachable section a few days back 
    def uniquePaths(self, m: int, n: int) -> int:
        # initial position is 0, 0
        
        # build out solution grid starting from destination
        grid = [[] for i in range(n)]
        for l in grid:
            for i in range(m):
                l.append(0)
        
        # start by putting ones on the right and bottom edges
        for i in range(n):
            grid[i][len(grid[0])-1] = 1
        
        for i in range(m):
            grid[len(grid)-1][i] = 1
        
        # fill out the rest of the grid following the rule that
        # grid[r][c] = grid[r+1][c] + grid[r][c+1]
        for r in range(len(grid)-2, -1,-1):
            for c in range(len(grid[0])-2,-1, -1):
                grid[r][c] = grid[r+1][c] + grid[r][c+1]
        # select the value at the start index (0,0)
        return grid[0][0]