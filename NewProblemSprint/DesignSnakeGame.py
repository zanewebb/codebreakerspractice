# this problem's test cases suck so much

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.snakeR = 0
        self.snakeC = 0
        self.snakebody = deque()
        
        self.food = deque(food)
        self.length = 0
        self.directions = {
            "U": [-1,0],
            "D": [1,0],
            "L": [0,-1],
            "R": [0,1]
        }
        self.grid = []
        print("height", height)
        print("width", width)
        for i in range(height):
            self.grid.append([""]*width)
         
        self.newFood()
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        # get new position
        newr = self.directions[direction][0] + self.snakeR
        newc = self.directions[direction][1] + self.snakeC
        # print("moving head",direction, "to new loc",newr,newc)
        
        # check for game over
        if newr < 0 or newr == len(self.grid) or newc < 0 or newc == len(self.grid[0]) or [newr,newc] in self.snakebody:
            return -1
        
        self.snakeR = newr
        self.snakeC = newc
        
        if self.grid[newr][newc] == "F":
            self.length += 1
            self.grid[newr][newc] = ""
            try:
                self.newFood()
            except:
                print("no")
            self.snakebody.appendleft([newr,newc])
        else:
            self.updateSnake(newr, newc)
        
        return self.length
        
    def newFood(self):
        if len(self.food) > 0:
            newfoodloc = self.food.popleft()
            print(newfoodloc)
            print([len(self.grid),len(self.grid[0])])
            self.grid[newfoodloc[0]][newfoodloc[1]] = "F"
        # print(self.grid, "\n\n\n")
    
    def updateSnake(self, nextr, nextc):
        # print(self.snakebody)
        if len(self.snakebody) > 0:
            tail = self.snakebody.pop()
            self.snakebody.appendleft([nextr,nextc])
            # print(self.snakebody)
        
        
class Node:
    def __init__(self, r = 0, c = 0):
        self.next = None
        self.r = r
        self.c = c

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)