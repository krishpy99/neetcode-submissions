class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        left, right = 0, len(s1) - 1
        ds1 = {}
        swds2 = {}

        for i in range(len(s1)):
            ds1[s1[i]] = ds1.get(s1[i], 0) + 1
            swds2[s2[i]] = swds2.get(s2[i], 0) + 1

        if ds1 == swds2:
            return True
        
        left += 1
        right += 1

        while right < len(s2):
            swds2[s2[left - 1]] -= 1
            if swds2[s2[left - 1]] == 0:
                del swds2[s2[left - 1]]
            swds2[s2[right]] = swds2.get(s2[right], 0) + 1
            if ds1 == swds2:
                return True
            left += 1
            right += 1
        
        return False