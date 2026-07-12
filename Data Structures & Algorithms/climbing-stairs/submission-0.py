class Solution:
    def climbStairs(self, n: int) -> int:
        
        a, b, c = 0, 1, 2
        if n == 1:
            return b
        if n == 2:
            return c
        
        for i in range(3, n + 1):
            a, b, c = b, c, b+c
        
        return c