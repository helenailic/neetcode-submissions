from collections import deque 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(row, col, grid, visited):
            queue = deque()
            visited.add((row, col))
            queue.append((row, col))
            while len(queue) != 0:
                row, col = queue.popleft()
                for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                    new_row = row + dr
                    new_col = col + dc
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and (new_row, new_col) not in visited and grid[new_row][new_col] == '1':
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))

        numIslands = 0
        visited = set() #stores tuples of (row, col)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in visited:
                    numIslands += 1
                    
                    #explore entire island with bfs 
                    bfs(row, col, grid, visited)
                    
        return numIslands