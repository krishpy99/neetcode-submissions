class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        while n not in d:
            d[n] = 1
            x = 0
            while n > 0:
                x += (n%10)**2
                n //= 10
            n = x
        
        return 1 in d