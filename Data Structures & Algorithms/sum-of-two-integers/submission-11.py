class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0x7ff
        while b != 0:
            tmp = ((a & b) << 1) & mask
            a = ((a^b) & mask)
            b = tmp
        
        if a > (1<<10):
            print(a, ~a)
            return ~(~a & 0x3ff)

        return a