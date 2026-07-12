from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = [[] for _ in range(n)]
        for i in flights:
            adj[i[0]].append([i[1], i[2]])
        
        q = deque([[src, -1, 0]])
        
        bestcost = -1

        while len(q) > 0:
            a = q[0]
            q.popleft()
            print(a)
            if a[1] > k:
                continue
            if a[0] == dst and (bestcost == -1 or bestcost > a[2]):
                bestcost = a[2]

            for i in adj[a[0]]:
                q.append([i[0], a[1] + 1, i[1] + a[2]])
        
        return bestcost