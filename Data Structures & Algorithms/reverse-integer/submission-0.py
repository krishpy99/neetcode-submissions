class Solution:
    def reverse(self, n: int) -> int:
        sign = None
        r = None
        if n < 0:
            r, sign, LIMIT = 0, -1, -1 * (1<<31)
            for i, j in enumerate(str(n)[1:]):
                NEW_LIMIT = LIMIT + r + int(j) * (10 ** int(i))
                if NEW_LIMIT > 0:
                    r = 0
                    break
                else:
                    r += int(j) * int(10 ** int(i))
            
        else:
            r, sign, LIMIT = 0, 1, (1<<31) - 1
            for i, j in enumerate(str(n)):
                NEW_LIMIT = LIMIT - r - int(j) * (10 ** int(i))
                if NEW_LIMIT < 0:
                    r = 0
                    break
                else:
                    r += int(j) * int(10 ** int(i))

        print(r, sign)
        return r * sign