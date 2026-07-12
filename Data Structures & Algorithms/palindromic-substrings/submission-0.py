class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]

        def rec(i, j):
            if i > j:
                return 0
            if dp[i][j] > -1:
                return dp[i][j]
            if s[i] != s[j]:
                dp[i][j] = 0
                return dp[i][j]

            if i == j or i == j-1:
                dp[i][j] = 1
            else:
                if rec(i+1, j-1):
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
            return dp[i][j]
            
        
        for i in range(len(s)):
            for j in range(len(s)):
                rec(i, j)

        c = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if dp[i][j] > 0:
                    c += 1
                    
        return c