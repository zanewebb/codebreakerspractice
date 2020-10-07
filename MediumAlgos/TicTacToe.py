
# much smarter way i found
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.cols = [0] * n
        self.rows = [0] * n
        self.diagonal = 0
        self.invdiagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        
        self.cols[col] += 1 if player == 1 else -1
        self.rows[row] += 1 if player == 1 else -1
        
        if row == col:
            self.diagonal += 1 if player == 1 else -1
        if row == self.n-col-1:
            self.invdiagonal += 1 if player == 1 else -1
        
        
        if self.n in [self.diagonal, self.invdiagonal, self.rows[row], self.cols[col]]:
            return 1
        elif -self.n in [self.diagonal, self.invdiagonal, self.rows[row], self.cols[col]]:
            return 2
        
        return 0
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)



# Not Working

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board = [[0]*n for i in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.board[row][col] = player
        return self.isWin()
        
    
    def isWin(self):
        colsDict = defaultdict(set)
        rowsDict = defaultdict(set)
        
        # for i in range(self.n):
            
        for r in range(0,len(self.board)):
            for c in range(0,len(self.board[r])):
                colsDict[c].add(self.board[r][c])
                rowsDict[r].add(self.board[r][c])
                
            if len(rowsDict[r]) == 1 and 0 not in rowsDict[r]:
                return rowsDict[r].pop()
        
        
        for i in range(self.n):
            if len(colsDict[i]) == 1 and 0 not in colsDict[i]:
                return colsDict[i].pop()
        
        # diagonal check only if odd # width and height
        prev = self.board[0][0]
        for i in range(1,self.n):
            if self.board[i][i] != prev:
                break
        else:
            if prev != 0:
                return prev
            
        prev = self.board[0][-1]
        for i in range(1,self.n):
            if self.board[i][-(i+1)] != prev:
                    break
        else:
            if prev != 0:
                return prev
            
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)