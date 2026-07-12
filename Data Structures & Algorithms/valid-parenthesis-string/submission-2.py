class Solution:
    def checkValidString(self, s: str) -> bool:
        cnt = 0
        esc = 0
        for i in s:
            if i == '(':
                cnt += 1
            elif i == ')':
                cnt -= 1
                while cnt < 0 and esc > 0:
                    esc -= 1
                    cnt += 1
                if cnt < 0:
                    return False
            else:
                esc += 1
        
        s = s[::-1]
        cnt, esc = 0, 0
        for i in s:
            if i == ')':
                cnt += 1
            elif i == '(':
                cnt -= 1
                while cnt < 0 and esc > 0:
                    esc -= 1
                    cnt += 1
                if cnt < 0:
                    return False
            else:
                esc += 1

        return True