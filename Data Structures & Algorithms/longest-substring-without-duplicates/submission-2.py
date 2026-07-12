class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        i = 0
        j = 0
        best = 0
        while i < len(s) and j < len(s):
            print(i,j,d,'*')
            while j < len(s) and s[j] not in d:
                d[s[j]] = 1
                j += 1
            best = max(best, j - i)
            print(i,j,d,'**')
            if j == len(s):
                break
            while i < len(s) and s[i] != s[j]:
                del d[s[i]]
                i += 1
            i += 1
            j += 1
            print(i,j,d,'***')
        return best