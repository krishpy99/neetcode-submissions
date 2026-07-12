class Solution:
    def create(self, s: str, op: int, cp: int) -> None:
        if op == 0 and cp == 0:
            self.st.add(s)
            return
        cnt = 0
        for i in s:
            if i == '(':
                cnt += 1
            else:
                cnt -= 1
        if cnt > 0:
            assert cp > 0
            self.create(s + ")", op, cp - 1)
        if op > 0:
            self.create(s + "(", op - 1, cp)
    def generateParenthesis(self, n: int) -> List[str]:
        self.st = set()
        self.create("", n, n)
        return list(self.st)