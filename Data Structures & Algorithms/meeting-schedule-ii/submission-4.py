"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: [x.end, x.start])
        h = []

        if len(intervals) == 0:
            return 0
        
        for i in intervals:
            if len(h) == 0:
                heapq.heappush(h, i.end)
                continue
            t = heapq.heappop(h)
            heapq.heappush(h, i.end)
            if t > i.start:
                heapq.heappush(h, t)
        
        return len(h)