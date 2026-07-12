class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        def count(n):
            cnt = 0
            while n > 0:
                cnt += n%2
                n //= 2
            return cnt
        
        for i in range(0, n + 1):
            res.append(count(i))
        
        return res