class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[0 for _ in text2] for _ in text1]
        for i in range(n):
            for j in range(m):
                if i > 0:
                    dp[i][j] = max(dp[i-1][j], dp[i][j])
                if j > 0:
                    dp[i][j] = max(dp[i][j-1], dp[i][j])
                if text1[i] == text2[j]:
                    if i*j > 0:
                        dp[i][j] = max(dp[i-1][j-1] + 1, dp[i][j])
                    else:
                        dp[i][j] = max(dp[i][j], 1)
        
        # for i in range(n):
        #     print(dp[i])
        print(n, m)
        return dp[n-1][m-1]