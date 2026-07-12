class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        dp = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
            
        def isValid(i, j):
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
                return False
            return True
        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            
            best = 1

            if isValid(i-1, j) and matrix[i][j] < matrix[i-1][j]:
                x = dfs(i-1, j)
                best = max(x + 1, best)
            
            if isValid(i+1, j) and matrix[i][j] < matrix[i+1][j]:
                x = dfs(i+1, j)
                best = max(x + 1, best)

            if isValid(i, j-1) and matrix[i][j] < matrix[i][j-1]:
                x = dfs(i, j-1)
                best = max(x + 1, best)

            if isValid(i, j+1) and matrix[i][j] < matrix[i][j+1]:
                x = dfs(i, j+1)
                best = max(x + 1, best)
            
            dp[i][j] = best
            return best
        
        best = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                best = max(best, dfs(i, j))
        
        return best

                
            
            