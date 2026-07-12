class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = [] # {temp, index}
        r = [0] * len(temperatures)

        for i, j in enumerate(temperatures):
            while len(s) > 0 and s[-1][0] < j:
                r[s[-1][1]] = i - s[-1][1]
                s.pop()
            s.append([j, i])
        
        return r