class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pp = []
        for i in range(len(p)):
            if p[i] == "*":
                continue
            if i < len(p) - 1 and p[i+1] == "*":
                pp.append(p[i:i+2])
            else:
                pp.append(p[i])

        dp = [[False for _ in range(len(pp) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True

        for j in range(1, len(pp) + 1):
            if len(pp[j-1]) == 2:
                dp[0][j] = True
            else:
                break

        for i in range(1, len(s) + 1):
            for j in range(1, len(pp) + 1):
                if len(pp[j - 1]) == 2:
                    dp[i][j] = dp[i][j-1]
                    if pp[j-1][0] == '.':
                        dp[i][j] |= (dp[i-1][j] or dp[i-1][j-1])
                    else:
                        dp[i][j] |= (dp[i-1][j] or dp[i-1][j-1]) and pp[j-1][0] == s[i-1]
                else:
                    if pp[j-1][0] == ".":
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        if pp[j-1][0] == s[i-1]:
                            dp[i][j] = dp[i-1][j-1]
                        else:
                            dp[i][j] = False
        print("     ", end = "   ")
        for i in pp:
            print(i, end = "   ")
        print()
        for i in dp:
            print(s[dp.index(i) - 1] if dp.index(i) > 0 else " ", end = " ")
            for j in i:
                print(j, end = " ")
            print()
        print()
        return dp[len(s)][len(pp)]