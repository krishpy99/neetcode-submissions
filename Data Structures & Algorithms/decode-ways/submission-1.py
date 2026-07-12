d = {}
class Solution:
    def numDecodings(self, s: str) -> int:
        global d
        if s in d:
            return d[s]
        if s is None or len(s) == 0:
            return 1
        t = 0
        t += (s[0] > '0') * self.numDecodings(s[1:])
        if len(s) > 1:
            t +=  (s[:2] <= "26" and s[:2] > "09") * self.numDecodings(s[2:])
        d[s] = t
        return t