class CountSquares:

    def __init__(self):
        self.points = []
        self.d = {}

    def add(self, point: List[int]) -> None:
        if tuple(point) not in self.d:
            self.points.append(point)
            self.d[tuple(point)] = 1
            return
        self.d[tuple(point)] += 1

    def count(self, point1: List[int]) -> int:
        cnt = 0
        for point4 in self.points:
            if point4[0] != point1[0] and point1[1] != point4[1]:
                point2 = (point1[0], point4[1])
                point3 = (point4[0], point1[1])
                if point2 in self.d and point3 in self.d:
                    cnt += self.d[point2] * self.d[point3] * self.d[tuple(point4)]
        return cnt