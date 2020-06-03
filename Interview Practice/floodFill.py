# first try, easy, same as number of islands

class Solution:
    def __init__(self):
        self.image = None
        self.newColor = None
        self.oldColor = None
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.oldColor = image[sr][sc]
        self.newColor = newColor
        self.image = image
        
        if self.oldColor == self.newColor:
            return self.image
        
        self.DFS(sr,sc)
        return self.image
    def DFS(self, r, c):
        if r >= 0 and c >= 0 and r < len(self.image) and c < len(self.image[0]) and self.image[r][c] == self.oldColor:
            self.image[r][c] = self.newColor
            
            self.DFS(r+1, c)
            self.DFS(r-1, c)
            self.DFS(r, c+1)
            self.DFS(r, c-1)