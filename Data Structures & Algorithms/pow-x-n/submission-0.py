class Solution:
    def myPow(self, x: float, n: int) -> float:
        y = 1
        neg = False
        if n < 0:
            n *= -1
            neg = True
        while n != 0:
            print(x, y, n)
            if n%2 != 0:
                y *= x
            x *= x
            n //= 2
        
        
        if neg:
            return 1 / y
        else:
            return y