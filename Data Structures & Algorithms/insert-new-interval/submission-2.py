class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)

        for i in range(len(intervals) - 1):
            if intervals[i] > intervals[-1]:
                intervals[i], intervals[-1] = intervals[-1], intervals[i]
        
        cnt = 0
        i = 1
        while i < len(intervals) - cnt:
            print(i, intervals[i])
            if cnt > 0 and i + cnt < len(intervals):
                intervals[i] = intervals[i+cnt]
                i += 1
                continue
            j = i
            while j < len(intervals) and intervals[i-1][1] >= intervals[j][0]:
                intervals[i-1][1] = max(intervals[i-1][1], intervals[j][1])
                j += 1
                cnt += 1
            print(i, j, cnt)
            if cnt == 0:
                i += 1
        
        while cnt > 0:
            intervals.pop()
            cnt -= 1
        
        return intervals