class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def recurse(i, cur, ar):
            if cur > target:
                return
            if cur == target:
                res.append(ar.copy())
                return
            
            for ii in range(i, len(nums)):
                j = nums[ii]
                ar.append(j)
                recurse(ii, cur + j, ar)
                ar.pop()
        
        recurse(0, 0, [])

        return res