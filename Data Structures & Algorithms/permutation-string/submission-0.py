class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = {}
        for i in s1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        
        i = 0
        j = len(s1) - 1
        while j < len(s2):
            d2 = {}
            print(i, j)
            for k in range(i, j+1):
                if s2[k] in d2:
                    d2[s2[k]] += 1
                else:
                    d2[s2[k]] = 1
            flag = True
            for it in d1.keys():
                if it not in d2 or d1[it] != d2[it]:
                    flag = False
            
            for it in d2.keys():
                if it not in d1 or d1[it] != d2[it]:
                    flag = False
            if flag:
                return True

            print(d1)
            print(d2)
            i += 1
            j += 1
        return False