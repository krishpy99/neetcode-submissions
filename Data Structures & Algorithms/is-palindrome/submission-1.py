class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        s = s.replace(' ', '')
        print(s)
        t = []
        for i in s:
            if i.isalnum():
                t.append(i)
        s = ''.join(t)
        print(s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True