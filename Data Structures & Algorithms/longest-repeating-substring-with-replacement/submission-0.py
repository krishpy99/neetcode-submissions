class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        i = 0
        j = 0 
        best = 0
        add = True
        while j < len(s):
            if add:
                if s[j] in d:
                    d[s[j]] += 1
                else:
                    d[s[j]] = 1
                j += 1
                cnt = 0
                sumd = 0
                for x in d:
                    cnt = max(cnt, d[x])
                    sumd += d[x]
                if sumd - cnt > k:
                    add = False
                else:
                    best = max(best, j - i)
            else:
                assert s[i] in d
                d[s[i]] -= 1
                i += 1
                if d[s[i]] == 0:
                    del d[s[i]]
                cnt = 0
                sumd = 0
                for x in d:
                    cnt = max(cnt, d[x])
                    sumd += d[x]
                if sumd - cnt <= k:
                    add = True
        return best