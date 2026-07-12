class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append([i, j])

        def works(i, j, l):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == -1:
                return
            
            if grid[i][j] > l + 1:
                grid[i][j] = l + 1
                q.append([i, j])
            

        cur = 0
        while len(q) - cur > 0:
            [i, j] = q[cur]
            works(i+1, j, grid[i][j])
            works(i-1, j, grid[i][j])
            works(i, j+1, grid[i][j])
            works(i, j-1, grid[i][j])
            cur += 1
        
        