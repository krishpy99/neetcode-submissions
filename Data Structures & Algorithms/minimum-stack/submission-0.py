class MinStack:

    def __init__(self):
        self.a = []
        self.b = []

    def push(self, val: int) -> None:
        self.a.append(val)
        if len(self.b) > 0:
            self.b.append(min(val, self.b[-1]))
        else:
            self.b.append(val)

    def pop(self) -> None:
        self.a.pop()
        self.b.pop()

    def top(self) -> int:
        #print(self.a)
        return self.a[-1]

    def getMin(self) -> int:
        #print(self.b)
        return self.b[-1]
