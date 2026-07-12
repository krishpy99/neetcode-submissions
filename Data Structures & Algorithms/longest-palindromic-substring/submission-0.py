class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        for i in range(len(s)):
            # for odd string

            k = i - 1
            l = i + 1
            while k >= 0 and l < len(s) and s[k] == s[l]:
                k -= 1
                l += 1
            
            if len(res) < l - k - 1:
                res = s[k+1: l]
            
            k = i
            l = i + 1
            while k >= 0 and l < len(s) and s[k] == s[l]:
                k -= 1
                l += 1
            
            if len(res) < l - k - 1:
                res = s[k+1: l]
        
        return res