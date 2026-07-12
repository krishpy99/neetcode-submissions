class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        cnt = 0
        v = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def dfs(i, j):
            nonlocal cnt
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or v[i][j] == 1 or grid[i][j] == 0:
                return
            
            v[i][j] = 1
            cnt += 1

            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
        
        best = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and v[i][j] == 0:
                    cnt = 0
                    dfs(i, j)
                    best = max(best, cnt)
        
        return best