class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()

        def recurse(i, cur, ar):
            if cur > target:
                return
            if cur == target:
                res.add(tuple(ar.copy()))
                return
            
            for ii in range(i, len(nums)):
                j = nums[ii]
                ar.append(j)
                recurse(ii + 1, cur + j, ar)
                ar.pop()
        
        recurse(0, 0, [])

        res = list(res)
        for i in range(0, len(res)):
            res[i] = list(res[i])

        return res