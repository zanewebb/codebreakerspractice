
# second time ?
def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    self.DFS(r,c, grid)
                    count += 1
        
        return count
    
    def DFS(self, r, c, grid):
        if r >= len(grid) or c >= len(grid[0]) or c < 0 or r < 0 or grid[r][c] != "1":
            return
        
        grid[r][c] = "X"
        
        self.DFS(r+1, c, grid)
        self.DFS(r-1, c, grid)
        self.DFS(r, c+1, grid)
        self.DFS(r, c-1, grid)0


# found this solution strat, works well, makes sense

class Solution:
    def __init__(self):
        self.grid = None
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        # set the grid to the class var for access in the DFS
        self.grid = grid    
        
        # track an island counter
        islands = 0
        
        # O(M*N) search across the grid:
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                # if the value at the position is a 1, begin the DFS on this position
                if self.grid[r][c] == "1":
                    self.DFS(r,c)
                    # increment the count
                    islands += 1
        
        return islands
                
    
    def DFS(self, row, col):
        # verify that the given row and col are within bounds
        # also check if we are still looking at an island, if not, return
        if row <0 or col < 0 or row >= len(self.grid) or col >= len(self.grid[0]) or self.grid[row][col] != "1":
            return
        
        # now that we know this position is a valid land tile, mark it as seen by changing its value
        self.grid[row][col] = "i"
        
        # kick off a DFS in all directions
        self.DFS(row + 1, col)
        self.DFS(row - 1, col)
        self.DFS(row, col + 1)
        self.DFS(row, col - 1)