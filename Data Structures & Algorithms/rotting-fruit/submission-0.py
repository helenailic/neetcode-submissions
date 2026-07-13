from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotting_pts = [] #list of tuples ()
        numFresh = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    numFresh += 1
                elif grid[row][col] == 2:
                    rotting_pts.append((row, col))

        if numFresh == 0:
            return 0

        q = deque() #store ((row, col), time)
        for pt in rotting_pts:
            q.append(((pt[0], pt[1]), 0))

        maxTime = 0
        while q:
            curr = q.popleft()
            maxTime = max(maxTime, curr[1])
            directions = ([-1, 0], [1, 0], [0, 1], [0, -1])
            for dr, dc in directions:
                nr = curr[0][0] + dr
                nc = curr[0][1] + dc
                if nr < len(grid) and nc < len(grid[0]) and nr >= 0 and nc >= 0 and grid[nr][nc] == 1:
                    q.append(((nr, nc), curr[1]+1)) 
                    grid[nr][nc] = 2
                    numFresh -= 1

        if numFresh != 0:
            return -1 
        return maxTime


