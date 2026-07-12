class Solution:
    def multiplyNumber(self, a: List[int], b: int) -> List[int]:
        a, r = a[::-1], []
        c = 0
        for i in a:
            r.append((i * b + c) % 10)
            c = (i * b + c) // 10
        
        if c > 0:
            assert(c < 10)
            r.append(c)
        
        return r[::-1]



    def add(self, a: List[int], b: List[int]) -> List[int]:
        a, b, r = a[::-1], b[::-1], []
        i = 0
        c = 0
        while i < len(a) and i < len(b):
            r.append((a[i] + b[i] + c) % 10)
            c = (a[i] + b[i] + c) // 10
            i += 1
        
        while i < len(a):
            r.append((a[i] + c) % 10)
            c = (a[i] + c) // 10
            i += 1
        
        while i < len(b):
            r.append((b[i] + c) % 10)
            c = (b[i] + c) // 10
            i += 1
        
        if c > 0:
            r.append(c)
        
        return r[::-1]

    def multiply(self, num1: str, num2: str) -> str:
        a = [int(i) for i in num1]
        b = [int(i) for i in num2][::-1]

        r = []
        for i, j in enumerate(b):
            rr = self.multiplyNumber(a, j)
            for _ in range(i):
                rr.append(0)
            r = self.add(r, rr)
        
        start = 0
        for i in r:
            if i == 0:
                start += 1
            else:
                break
        return ''.join([str(i) for i in r[min(start, len(r) - 1):]])


