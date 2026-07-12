class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += c
            if digits[i] > 9:
                c = digits[i]//10
                digits[i] %= 10
            else:
                c = 0
                break
        
        if c > 0:
            digits = digits[::-1]
            digits.append(c)
            digits = digits[::-1]
        return digits