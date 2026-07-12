class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fr = nums.copy()
        re = nums.copy()
        for i in range(1, len(fr)):
            fr[i] *= fr[i-1]
        for i in range(len(re) - 2, 0, -1):
            re[i] *= re[i+1]
        for i in range(len(nums)):
            p = 1
            p *= fr[i-1] if i > 0 else 1
            p *= re[i+1] if i < len(nums) - 1 else 1
            nums[i] = p
        return nums