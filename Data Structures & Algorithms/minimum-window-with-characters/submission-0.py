class Solution:
    def minWindow(self, s: str, t: str) -> str:
        q = [0] * 26
        Q = [0] * 26
        a = [0] * 26
        A = [0] * 26
            

        def addChar(x, X, ch):
            if ch.isupper():
                X[ord(ch) - ord('A')] += 1
            else:
                x[ord(ch) - ord('a')] += 1
        
        def remChar(x, X, ch):
            if ch.isupper():
                X[ord(ch) - ord('A')] -= 1
            else:
                x[ord(ch) - ord('a')] -= 1

        for i in t:
            addChar(a, A, i)

        def compare(x, X, y, Y):
            for i in range(26):
                if x[i] < y[i] or X[i] < Y[i]:
                    return 0
            
            return 1

        i = 0
        j = 0
        resi = 0
        resj = 0
        reslen = -1

        while j < len(s):

            chg = 0
            while j < len(s) and compare(q, Q, a, A) == 0:
                addChar(q, Q, s[j])
                if compare(q, Q, a, A) == 1:
                    chg = 1
                j += 1
            
            while compare(q, Q, a, A) == 1:
                remChar(q, Q, s[i])
                i += 1

            if chg and (reslen == -1 or j - i + 1 < reslen):
                resi = i - 1
                resj = j
            
        return s[resi: resj]

            
        return r