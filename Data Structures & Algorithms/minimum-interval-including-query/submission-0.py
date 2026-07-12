import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sorted_queries = [[j, i] for i,j in enumerate(queries)]
        sorted_queries.sort()
        intervals.sort()
        outputs = [-1 for _ in range(len(queries))]
        h = []
        for [i, j] in sorted_queries:
            while len(h) > 0:
                x = h[0]
                if not (x[1] <= i and x[2] >= i):
                    heapq.heappop(h)
                else:
                    break 
            for k in intervals:
                if k[0] <= i and k[1] >= i:
                    heapq.heappush(h, [k[1] - k[0] + 1, k[0], k[1]])

            while h:
                x = h[0]
                if not (x[1] <= i and x[2] >= i):
                    heapq.heappop(h)
                else:
                    break 
            
            if h:
                outputs[j] = h[0][0]
        
        return outputs