class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) + len(s3) == 0:
            return True
        if len(s1) + len(s2) != len(s3):
            return False
        
        if len(s1) * len(s2) == 0:
            if len(s1) != 0:
                return s1 == s3
            else:
                return s2 == s3
        
        dp = [[-1 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[0][0] = True

        for i in range(1, len(s1)+1):
            dp[i][0] = s1[:i] == s3[:i]
        for i in range(1, len(s2)+1):
            dp[0][i] = s2[:i] == s3[:i]
        
        def check(i, j):
            if i == -1 or j == -1:
                return False
            if dp[i-1][j] == -1:
                check(i-1, j)
            if dp[i][j-1] == -1:
                check(i, j-1)
            x = dp[i-1][j]
            y = dp[i][j-1]
            if (x and s1[i-1] == s3[i+j-1]) or (y and s2[j-1] == s3[i+j-1]):
                dp[i][j] = True
                return True
            dp[i][j] = False
            return False
        
        ans = check(len(s1), len(s2))

        for i in range(len(s1)):
            for j in range(len(s2)):
                print("{", s1[:i+1], " ", s2[:j+1], " ", dp[i][j], "}", end=" ")
            
            print()

        return ans

