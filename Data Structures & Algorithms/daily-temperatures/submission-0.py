class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while len(a) > 0:
                p = a[-1]
                if p[0] < temperatures[i]:
                    a.pop()
                    res[p[1]] = i - p[1]
                else:
                    break
            a.append([temperatures[i], i])
        return res