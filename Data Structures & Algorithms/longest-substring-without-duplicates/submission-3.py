class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        ds = {}
        maxlen = 0
        while right < len(s):
            while s[right] in ds:
                del ds[s[left]]
                left += 1
            
            ds[s[right]] = True
            print(left, right)
            maxlen = max(maxlen, right - left + 1)
            right += 1
        
        return maxlen
            



# -> zxyz <-