class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {}
        v = {}
        for i in nums:
            m[i] = 1
            v[i] = 0

        best = 0
        
        for i in m.keys():
            if v[i] == 1:
                continue
            v[i] = 1
            cnt = 1

            j = i
            while j - 1 in m:
                cnt += 1
                v[j-1] = 1
                j -= 1
            
            j = i
            while j + 1 in m:
                cnt += 1
                v[j+1] = 1
                j += 1
                
            best = max(best, cnt)
        
        return best