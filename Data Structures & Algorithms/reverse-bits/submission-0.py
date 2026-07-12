class Solution:
    def reverseBits(self, n: int) -> int:
        res = []
        while n > 0:
            res.append(n%2)
            n //= 2
        
        while len(res) < 32:
            res.append(0)
        x = 0
        y = 1
        for i in res[::-1]:
            x += i*y
            y *= 2
        
        return x