class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(t))]

        for i in range(len(t)):
            for j in range(len(s)):
                if j > 0:
                    dp[i][j] += dp[i][j-1]
                if s[j] == t[i]:
                    if i > 0 and j > 0:
                        dp[i][j] += dp[i-1][j-1]
                    elif j >= i:
                        dp[i][j] += 1
        
        print("  ", end="")
        for i in s:
            print(i, end = " ")
        print()
        for i in range(len(t)):
            print(t[i], end = " ")
            for j in range(len(s)):
                print(dp[i][j], end = " ")
            print()

        return dp[len(t) - 1][len(s) - 1]