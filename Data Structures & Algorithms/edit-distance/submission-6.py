class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) * len(word2) == 0:
            return len(word1) + len(word2)
            
        dp = [[101 for _ in range(len(word2)+1)] for _ in range(len(word1) +1)]
        dp[0][0] = 0
        for i in range(len(word1)):
            dp[i+1][0] = i+1
        for j in range(len(word2)):
            dp[0][j+1] = j+1
            
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                dp[i][j] = min(dp[i-1][j-1] + (word1[i-1] != word2[j-1]), dp[i][j])
                dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
                dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
        
        print("    ", end="")
        for i in word2:
            print(i, end= " ")
        
        print()
        for i in range(len(word1) + 1):
            print(" " if i == 0 else word1[i-1] , end=" ")
            for j in range(len(word2) + 1):
                print(dp[i][j], end=" ")
            print()
        
        return dp[len(word1)][len(word2)]