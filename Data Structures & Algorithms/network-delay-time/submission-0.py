import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = [[] for _ in range(n)]

        for [i, j, t] in times:
            edges[i-1].append([j-1, t])

        q = [[0, k-1]]

        btt = 0
        d = {}
        while len(q) > 0:
            [tt, curr] = heapq.heappop(q)
            if curr in d and tt > d[curr]:
                continue
            d[curr] = tt
            edges[curr].sort(key = lambda x: x[1])
            btt = max(btt, tt)
            for i in edges[curr]:
                heapq.heappush(q, [tt + i[1], i[0]])
        
        for i in range(n):
            if i not in d:
                return -1
        
        return btt