class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        v = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def dfs2d(i, j):
            if i < 0 or j < 0:
                return
            if i >= len(grid) or j >= len(grid[0]):
                return
            
            if v[i][j] == 1:
                return
            if grid[i][j] == "0":
                return

            v[i][j] = 1

            dfs2d(i+1, j) 
            dfs2d(i, j+1) 
            dfs2d(i-1, j) 
            dfs2d(i, j-1) 
        
        cnt = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if v[i][j] == 0 and grid[i][j] == "1":
                    cnt += 1
                    dfs2d(i, j)
        
        return cnt