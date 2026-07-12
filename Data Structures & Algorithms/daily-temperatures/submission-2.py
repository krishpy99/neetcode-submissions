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

# s => [[30, 0]]
# s => [[38, 1]] r[0] = 1 - 0 = 1
# s => [[38, 1], [30,2]]
# s => [[38, 1], [36, 3]] r[2] = 3 - 2 = 1
# s => [[38, 1], [36, 3], [35, 4]]
# s => [[40, 5]] r[4] = 5 - 4 = 1, r[3] = 5 - 3 = 2, r[1] = 5 - 1 = 4
# s => [[40, 5], [28, 6]]