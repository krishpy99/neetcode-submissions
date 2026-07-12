class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffff
        while b != 0:
            tmp = ((a & b) << 1) & mask
            a = ((a^b) & mask)
            b = tmp
        
        if a > (1<<15):
            print(a, ~a)
            return ~(~a & 0x7fff)

        return a