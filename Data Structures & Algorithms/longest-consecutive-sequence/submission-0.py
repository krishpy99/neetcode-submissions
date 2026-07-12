class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        cnt = 0
        temp = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if i > 0 and nums[i] != nums[i-1] + 1:
                cnt = max(cnt, temp)
                temp = 0
            temp += 1
        cnt = max(cnt, temp)
        return cnt