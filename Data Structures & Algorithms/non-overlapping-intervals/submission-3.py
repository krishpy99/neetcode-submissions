import heapq

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda p : p[1])
        
        l = intervals[0][1]
        cnt = 0
        for i in range(1, len(intervals)):
            if l > intervals[i][0]:
                cnt += 1
                continue
            l = intervals[i][1]
        
        return cnt