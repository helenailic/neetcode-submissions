from collections import deque 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #max area of island! 
        #same thing but now you do it helena
        def bfs(row, col, grid, visited, maxArea):
            area = 1
            queue = deque()
            queue.append((row, col))
            visited.add((row, col))
            #check each side of the 4 if 1s, add it
            while len(queue) != 0:
                row, col = queue.popleft()
                for dr, dc in ((0, -1), (0, 1), (-1, 0), (1,0)):
                    new_row = row + dr
                    new_col = col + dc 
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                        area += 1
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
            maxArea = max(area, maxArea)
            return maxArea

        visited = set()
        maxArea = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    #bfs on all of it
                    maxArea = bfs(row, col, grid, visited, maxArea)

        return maxArea 