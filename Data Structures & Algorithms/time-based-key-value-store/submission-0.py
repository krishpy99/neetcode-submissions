class TimeMap:

    def __init__(self):
        self.d = {}
        self.km = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[(timestamp, key)] = value
        if key not in self.km:
            self.km[key] = []
        self.km[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.km:
            return ""

        print(key, self.km)
        lo = -1
        hi = len(self.km[key]) - 1

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if self.km[key][mid] > timestamp:
                hi = mid - 1
            else:
                lo = mid
        
        if lo == -1:
            return ""
        else:
            return self.d[(self.km[key][lo], key)]
