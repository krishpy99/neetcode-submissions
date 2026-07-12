class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        m = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def rec(i, s):
            if i == len(digits):
                if s != "":
                    res.append(s)
                return
            
            for j in m[digits[i]]:
                rec(i+1, s + j)
        
        rec(0, "")
        return res