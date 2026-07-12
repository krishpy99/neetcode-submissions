import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        heapq.heapify(h)

        for i in stones:
            heapq.heappush(h, -i)
        
        while len(h) > 1:
            a = heapq.heappop(h)
            b = heapq.heappop(h)
            if -a > -b:
                heapq.heappush(h, a-b)
            elif -a < -b:
                heapq.heappush(h, b-a)
        
        if len(h) > 0:
            return -heapq.heappop(h)
        return 0