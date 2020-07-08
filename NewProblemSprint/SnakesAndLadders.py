# got it!
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        seen = {1 : 0} # we've seen space 1, we know it takes 0 steps to get there
        opportunities = deque([1]) # we have yet to finish exploring from space 1, the start
        
        while opportunities:
            currentspace = opportunities.popleft()
            
            for space in range(currentspace + 1, currentspace + 7): #covers 6 total spaces
                
                # need to do some trickery to figure out what this space NUMBER equates to in row and col
                row = (space-1) // len(board)
                col = (space-1) % len(board)
                boardval = board[~row][col if row % 2 == 0 else ~col]
                
                # if this is a snake or ladder, travel to the space indicated
                if boardval > 0:
                    space = boardval
                
                # if we've reached the end of the board, return the answer
                if space == len(board) ** 2:
                    return seen[currentspace] + 1
                
                # if we havent seen this space, set the step count to it
                if space not in seen:
                    seen[space] = seen[currentspace] + 1
                    # also be sure to tag it as an opportunity to investigate
                    opportunities.append(space)
                
        # we must have not reached the end if we investigated all opportunities
        return -1
        
        


# this is really hard, had to copy a lot
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        possiblepaths = deque([1])
        # we know that initially we start at space 1
        seen = {1:0}
        
        while possiblepaths:
            curspace = possiblepaths.popleft()
            for i in range(curspace + 1, curspace + 7):
                h = (i - 1) // len(board) # vertically it will be a multiple of n
                w = (i - 1) % len(board) # offset horizontally
                
                nextspace = board[~h][w if h % 2 == 0 else ~w] 
                
                # if this spot is a snake or ladder, move there
                if nextspace > 0:
                    i = nextspace
                    
                if i == len(board)**2:
                    return seen[curspace] + 1
                
                if i not in seen:
                    seen[i] = seen[curspace] + 1
                    possiblepaths.append(i)
                    
        return -1
                
                


# lee215's ans
def snakesAndLadders(self, board):
    #  height and width of the board
        n = len(board)

        # need are the steps we've taken ???
        need = {1: 0}
        # this is the list of paths we're considering
        bfs = [1]
        # bfs will continue to expand, this is the same as using while len() > 0 and popping i think
        for x in bfs:
            # consider each dice roll, 1 - 6
            for i in range(x + 1, x + 7):
                # determine the row and column. Row (a) is determined by our space number / n
                # we then acces the row index FROM THE OPPOSITE END. space 1 would equate to a = (1-1) / 6 = 0
                # which would access the bottom row

                # in determining the column we use modulo, and decide which side to access the row from
                # based on if the row is an even row
                a, b = (i - 1) / n, (i - 1) % n
                nxt = board[~a][b if a % 2 == 0 else ~b]

                # Decisions

                # if the next spot we're evaluating is a snake or ladder, go there
                if nxt > 0: i = nxt

                # if the spot we're at is the finish, add 1 to this path's steps and finish (return)
                if i == n * n: return need[x] + 1

                # if the next position has not been considered, add it to our dict of considered spots with
                # an additional step count. After doing that, add that step to our BFS stack to be considered in the future
                if i not in need:
                    need[i] = need[x] + 1
                    bfs.append(i)

        # if we didnt return by finding the finish, return -1 to indicate that it wasn't possible
        return -1


#LC is failing to send my solution so i cant test it, pretty sure it doesnt fully work

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        boarddict = {}
        
        right = True
        i = 1
        for r in range(len(board)-1, -1, -1):
            c = 0 if right else len(board[0])-1
            
            while c < len(board[0]) and right:
                boarddict[i] = (r,c)
                board[r][c] = float("-inf") if board[r][c] < 0 else board[r][c]
                i += 1
                c += 1
            
            while c >= 0 and not right:
                boarddict[i] = (r,c)
                board[r][c] = float("-inf") if board[r][c] < 0 else board[r][c]
                i += 1
                c -= 1
            
            right = not right
            
        print(board)
        
        # DP solution ?
        # traverse the board, marking each cell encountered with the min number of steps
        # seen thus far. When a ladder or snake is encountered, update that location to our
        # current step -1 because that would be the end of the move. We count our steps
        # in negatives. 
        step = -1
        substep = 0
        for i in range(1,len(board)*len(board)+1):
            r, c = boarddict[i]
            
            if board[r][c] > 0:
                tempr, tempc = boarddict[board[r][c]]
                board[tempr][tempc] = max(step - 1, board[tempr][tempc])
                board[r][c] = float("-inf")
            
            if board[r][c] >= step:
                substep = 0
                step = board[r][c]
            else:
                board[r][c] = step
            
            substep += 1
            if substep == 6:
                step -= 1
                substep = 0
            
        print(board)
        
        return board[0][0] * -1
        
        