# slow but got it first time

class Solution:
    def __init__(self):
        self.dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        self.word = None
        self.board = None
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.word = word
        self.board = board
        
        startlocs = []
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    startlocs.append((r,c))
        if len(word) == 1 and len(startlocs) > 0:
            return True
        
        for loc in startlocs:
            if self.search(loc[0], loc[1], 1, set()):
                return True
        
    def search(self, r, c, i, seen):
        seen.add((r,c))
        
        if i == len(self.word):
            return True
        
        found = False
        
        for d in self.dirs:
            newr = r + d[0]
            newc = c + d[1]
            # print("checking ",newr,newc)
            if newr >= 0 and newr < len(self.board) and newc >=0 and newc < len(self.board[0]) and (newr,newc) not in seen and  self.board[newr][newc] == self.word[i]:
                # print("found",self.board[newr][newc], "at",newr,newc)
                found = found or self.search(newr, newc, i + 1, seen.copy())
        
        return found
        