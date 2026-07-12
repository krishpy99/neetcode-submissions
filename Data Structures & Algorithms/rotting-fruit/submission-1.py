class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        v = grid
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    v[i][j] *= -1
                    q.append([i, j, 0])
        
        start = 0

        def check(x, y):
            if x < 0 or y < 0:
                return False
            if x >= len(grid) or y >= len(grid[0]):
                return False
            if v[x][y] <= 0:
                return False
            return True
        
        mt = 0
        count = 100
        while len(q) - start > 0:
            s = q[start]
            mt = max(mt, s[2])
            x, y = s[0], s[1]
            count -= 1
            if count < 0:
                break
            #print(s[0], s[1], s[2], v[x][y])
            if v[x][y] >= 0:
                v[x][y] *= -1
            if check(x+1, y):
                q.append([x+1, y, s[2] + 1])
            if check(x, y+1):
                q.append([x, y+1, s[2] + 1])
            if check(x, y-1):
                q.append([x, y-1, s[2] + 1])
            if check(x-1, y):
                q.append([x-1, y, s[2] + 1])
            
            start += 1
        
        for i in v:
            for j in i:
                if j > 0:
                    return -1

        return mt