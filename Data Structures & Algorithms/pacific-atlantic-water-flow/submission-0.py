class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p = [[-1 for _ in heights[0]] for _ in heights]
        a = [[-1 for _ in heights[0]] for _ in heights]

        def dfs(i, j, previ, prevj):
            if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]) or heights[i][j] > heights[previ][prevj]:
                return False
            # print(f"({i},{j})-[{p[i][j]},{a[i][j]}]", end=" -> ")
            # if i == 2 and j == 1:
            #     print("DEBUG2", i, j, a[i][j], p[i][j])
            if previ == 1 and prevj == 1:
                print("DEBUG", i, j, a[i][j], p[i][j])
            if p[i][j] != -1:
                return True
            p[i][j] = 0
            a[i][j] = 0
            if i == 0 or j == 0:
                p[i][j] = 1
            if i == len(heights) - 1 or j == len(heights[0]) - 1:
                a[i][j] = 1
            
            if dfs(i+1, j, i, j):
                p[i][j] |= p[i+1][j]
                a[i][j] |= a[i+1][j]
            if dfs(i-1, j, i, j):
                p[i][j] |= p[i-1][j]
                a[i][j] |= a[i-1][j]
            if dfs(i, j+1, i, j):
                p[i][j] |= p[i][j+1]
                a[i][j] |= a[i][j+1]
            if dfs(i, j-1, i, j):
                p[i][j] |= p[i][j-1]
                a[i][j] |= a[i][j-1]
            return True
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if p[i][j] == -1:
                    dfs(i, j, i, j)
                    print()
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                print(p[i][j], end=" ")
            print()
        print()
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                print(a[i][j], end=" ")
            print()
        
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if p[i][j] and a[i][j]:
                    res.append([i, j])
        
        return res