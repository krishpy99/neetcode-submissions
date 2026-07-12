class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exists = {}
        for i in nums:
            exists[i] = True
        
        lcs = {}

        def rec(ele):
            if ele not in exists:
                return 0
            if ele not in lcs:
                lcs[ele] = rec(ele-1)+1
            return lcs[ele]
        
        maxlen = 0
        for i in nums:
            maxlen = max(maxlen, rec(i))
        
        return maxlen