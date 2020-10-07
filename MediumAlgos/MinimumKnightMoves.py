class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        return self.move(abs(x), abs(y))
    
    # this LRU cache trick is key to runtime, pretty crazy stuff
    @lru_cache(None)
    def move(self, x, y):
        if x + y == 0:
            return 0
        elif x + y == 2:
            return 2
        elif x + y == 1:
            return 3
        else:
            return min(self.move(abs(x-1), abs(y-2)), self.move(abs(x-2),abs(y-1))) + 1
        
        