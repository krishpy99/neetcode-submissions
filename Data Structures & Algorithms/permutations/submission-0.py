class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        s = set()
        def recurse(indices, arr, res):
            if len(indices) == 0:
                s.add(tuple(res))
                return
            for i in indices:
                x = indices.copy()
                x.remove(i)
                res.append(arr[i])
                recurse(x, arr, res.copy())
                res.pop()
        
        recurse([i for i in range(len(nums))], nums, [])

        return [list(i) for i in s]