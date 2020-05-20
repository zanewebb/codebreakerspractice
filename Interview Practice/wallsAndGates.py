class Solution:

   # accepted BFS solution
   def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # store all the gate locations
        queue = []
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    queue.append([r,c])
        
        # go over the locations, marking their distance from the gates until they are out of bounds
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        while len(queue) > 0:
            loc = queue.pop(0)
            
            for d in dirs:
                r = loc[0] + d[0]
                c = loc[1] + d[1]
                
                # skip this location if it is out of bounds or a wall
                if r < 0 or c < 0 or r >= len(rooms) or c >= len(rooms[0]) or rooms[r][c] != 2147483647:
                    continue
                
                rooms[r][c] = rooms[loc[0]][loc[1]] + 1
                queue.append([r,c])
                

   # shitty attempt

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] > 2147483646 and rooms[r][c] != -1:
                    self.findGate(r, c, r, c, 0, rooms)
        
    def findGate(self, r, c, curR, curC, dist, rooms):
        print(r,c,curR,curC,dist)
        print(rooms)
        if curR < 0 or curC < 0 or curR >= len(rooms) or curC >= len(rooms[0]) or rooms[curR][curC] == -1:
            return
        
        # set the min distance
        if rooms[curR][curC] == 0:
            rooms[r][c] = min(rooms[r][c], dist)
        
        self.findGate(r, c, curR+1, curC, dist+1, rooms)
        self.findGate(r, c, curR-1, curC, dist+1, rooms)
        self.findGate(r, c, curR, curC+1, dist+1, rooms)
        self.findGate(r, c, curR, curC-1, dist+1, rooms)