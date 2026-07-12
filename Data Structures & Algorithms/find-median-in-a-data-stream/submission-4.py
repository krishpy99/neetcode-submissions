import heapq

class MedianFinder:

    def __init__(self):
        self.minh = []
        self.maxh = []
        self.median = None
        self.n = 0       

    def addNum(self, num: int) -> None:
        self.n += 1
        
        if self.median is None:
            if (self.minh == [] and self.maxh == []) or (self.minh[0] > num and -self.maxh[0] < num):
                print("here", num)
                self.median = num
                return
            print("added number")
            if self.minh[0] < num:
                heapq.heappush(self.minh, num)
                self.median = heapq.heappop(self.minh)
            else:
                heapq.heappush(self.maxh, -num)
                self.median = -heapq.heappop(self.maxh)
        else:
            if num > self.median:
                heapq.heappush(self.maxh, -self.median)
                heapq.heappush(self.minh, num)
            else:
                heapq.heappush(self.minh, self.median)
                heapq.heappush(self.maxh, -num)
            self.median = None

    def findMedian(self) -> float:
        print(self.n, self.minh, self.maxh)
        if self.n % 2 == 1:
            return self.median
        else:
            return (1.0 * (self.minh[0] - self.maxh[0])) / 2
        