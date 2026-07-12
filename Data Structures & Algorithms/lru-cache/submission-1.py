from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.d = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        val = self.d[key]
        del self.d[key]
        self.d[key] = val
        return val        

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            del self.d[key]
        
        while len(self.d) >= self.capacity:
            del self.d[next(iter(self.d))]
        
        self.d[key] = value