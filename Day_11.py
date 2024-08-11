# https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/?envType=daily-question&envId=2024-08-11

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def count_islands():
            visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
            island_count = 0
            
            def dfs(x, y):
                stack = [(x, y)]
                visited[x][y] = True
                while stack:
                    cx, cy = stack.pop()
                    for dx, dy in directions:
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visited[nx][ny] and grid[nx][ny] == 1:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
            
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1 and not visited[i][j]:
                        island_count += 1
                        dfs(i, j)
            
            return island_count

        if count_islands() != 1:
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        return 1
                    grid[i][j] = 1

        return 2
