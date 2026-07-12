import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        

        v = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        q = []
        heapq.heappush(q, [grid[0][0],0, 0])
        t = 0
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        while len(q) > 0:
            f = heapq.heappop(q)
            dp[f[1]][f[2]] = f[0]
            v[f[1]][f[2]] = 1

            if f[1] + 1 >= 0 and f[1] + 1 < len(grid) and v[f[1]+1][f[2]] == 0:
                heapq.heappush(q, [max(grid[f[1]+1][f[2]], dp[f[1]][f[2]]), f[1] + 1, f[2]])
            if f[1] - 1 >= 0 and f[1] - 1 < len(grid) and v[f[1]-1][f[2]] == 0:
                heapq.heappush(q, [max(grid[f[1]-1][f[2]], dp[f[1]][f[2]]), f[1] - 1, f[2]])
            if f[2] + 1 >= 0 and f[2] + 1 < len(grid[0]) and v[f[1]][f[2]+1] == 0:
                heapq.heappush(q, [max(grid[f[1]][f[2]+1], dp[f[1]][f[2]]), f[1], f[2] + 1])
            if f[2] - 1 >= 0 and f[2] - 1 < len(grid[0]) and v[f[1]][f[2]-1] == 0:
                heapq.heappush(q, [max(grid[f[1]][f[2]-1], dp[f[1]][f[2]]), f[1], f[2] - 1])
        
        return dp[len(grid) - 1][len(grid[0]) - 1]