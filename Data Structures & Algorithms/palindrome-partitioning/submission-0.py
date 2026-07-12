class Solution:
    def partition(self, s: str) -> List[List[str]]:
        mem = {}

        def rec(i):
            if i in mem:
                return mem[i]
            if i >= len(s):
                return tuple()
            ss = []
            res = []
            for j in range(i, len(s)):
                ss.append(s[j])
                if ss == ss[::-1]:
                    rest = rec(j+1)
                    #print(i, "rest", rest, "ss", ss)
                    for k in rest:
                        a = [''.join(ss)]
                        a.extend(k)
                        res.append(a)
                #print(i, res)
            
            if ss == ss[::-1]:
                res.append([''.join(ss)])
            
            mem[i] = tuple(res)
            #print(i, res)
            return res

        return rec(0)