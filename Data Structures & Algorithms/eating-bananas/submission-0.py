class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(x):
            h1 = 0
            for i in piles:
                h1 += (i + x - 1) // x
            if h1 <= h:
                return True
            return False
        
        lo = 1
        hi = int(1e9)

        while lo < hi:
            mid = (lo + hi) // 2
            #print(lo, hi, mid)
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo