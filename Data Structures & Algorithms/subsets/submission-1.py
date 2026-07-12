class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        s = set()
        def recurse(i, nums, arr):
            if i == len(nums):
                s.add(tuple(sorted(arr)))
                return
            x = arr.copy()
            x.append(nums[i])
            recurse(i+1, nums, x)
            x.pop()
            recurse(i+1, nums, x)
        
        recurse(0, nums, [])

        return [list(i) for i in s]
        