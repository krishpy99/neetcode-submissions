import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = []
        
        d = {}
        for i in tasks:
            d[i] = d.get(i, 0) + 1
        
        for i, j in d.items():
            heapq.heappush(h, [1, -j, i])
        
        t = 1
        while len(h) > 0:
            x = []
            while len(h) > 0 and h[0][0] <= t:
                hh = heapq.heappop(h)
                x.append([hh[1], hh[0], hh[2]])
            if len(x) > 0:
                x.sort()
                x[0][0] += 1
                x[0][1] = t + n + 1
                print("x", t, x[0][2], x[0][0])
                for i in x:
                    if i[0] < 0:
                        heapq.heappush(h, [i[1], i[0], i[2]])
            else:
                hh = heapq.heappop(h)
                t = hh[0]
                print("y", t, hh[2], hh[1] + 1)
                if hh[1] + 1 < 0:
                    heapq.heappush(h, [t + n + 1, hh[1] + 1, hh[2]])
            t += 1
        


            
            
        
        return t - 1