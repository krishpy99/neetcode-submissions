class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1: 
            return ["()"]
        else:
            l = self.generateParenthesis(n-1)
            s = set()
            for i in l:
                cnt = 0
                for j in range(len(i)):
                    if cnt == 0:
                        s.add("(" + i[:j+1] + ")" + i[j+1:])
                        s.add(i[:j+1] + "()" + i[j+1:])
                        s.add(i[:j+1] + "(" + i[j+1:] + ")")
                    if i[j] == '(':
                        cnt += 1
                    else:
                        cnt -= 1
                if cnt == 0:
                    s.add("(" + i[:j+1] + ")" + i[j+1:])
                    s.add(i[:j+1] + "()" + i[j+1:])
                    s.add(i[:j+1] + "(" + i[j+1:] + ")")
                    
            return list(s)
