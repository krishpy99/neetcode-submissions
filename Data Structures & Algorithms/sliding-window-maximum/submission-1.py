import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        res = []
        for i, j in enumerate(nums):
            heapq.heappush(h, (-j, i))
            if i >= k - 1:
                while h[0][1] <= i - k:
                    heapq.heappop(h)
                res.append(-h[0][0])
        
        return res