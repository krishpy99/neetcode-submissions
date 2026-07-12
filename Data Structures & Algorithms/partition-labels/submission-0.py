class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i, j in enumerate(list(s)):
            d[j] = i
        
        prev = -1
        c = 0
        res = []
        for i, j in enumerate(list(s)):
            c = max(c, d[j])
            print(i, j, prev, c)
            if c <= i:
                print(i, j, prev, c, "check")
                res.append(c - prev)
                prev = i
            
        return res