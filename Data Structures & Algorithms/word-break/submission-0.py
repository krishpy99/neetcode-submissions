class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [-1 for _ in s]
        def recurse(i):
            if i == len(s):
                return True
            if dp[i] != -1:
                return dp[i]
            ss = ""
            for j in range(i, len(s)):
                ss += s[j]
                if ss in wordDict and recurse(j+1):
                    dp[i] = True
                    return dp[i]
            
            dp[i] = False
            return False
        
        return recurse(0)