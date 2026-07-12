class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [0] * len(position)
        for i in range(len(speed)):
            time[i] = [position[i], (target - position[i]) / speed[i]]
        time = sorted(time)
        a = []
        for i in range(len(time)):
            while len(a) > 0:
                if a[-1] <= time[i][1]:
                    a.pop()
                else:
                    break
            a.append(time[i][1])
        return len(a)