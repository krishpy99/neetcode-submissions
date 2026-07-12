import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        h = []

        def dist(i, j):
            return abs(i[0] - j[0]) + abs(i[1] - j[1])

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                heapq.heappush(h, [dist(points[i], points[j]), i, j])
        
        for i in h:
            print(i)
        
        d = [i for i in range(len(points))]
        cost = 0
        while len(h) > 0:
            t = heapq.heappop(h)
            x = t[1]
            y = t[2]
            while x != d[x]:
                x = d[x]
            while y != d[y]:
                y = d[y]
            if x != y:
                d[x] = min(x, y)
                d[y] = min(x, y)
                cost += t[0]
        
        return cost