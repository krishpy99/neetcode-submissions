class Solution:

    def encode(self, strs: List[str]) -> str:
        strs.append(str(len(strs)))
        return "%yadhu".join(strs)
    def decode(self, s: str) -> List[str]:
        st = s.split('%yadhu')
        if len(st) == 1:
            return []
        return st[:-1]