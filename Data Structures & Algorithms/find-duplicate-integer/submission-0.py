class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for i, j in enumerate(nums):
            if j != i + 1:
                if nums[j-1] == j:
                    return j
                nums[i], nums[j-1] = nums[j-1], nums[i]