class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = 0, 0, 0
        [x, y, z] = target
        for [i, j, k] in triplets:
            if i <= x and j <= y and k <= z:
                a, b, c = max(a, i), max(b, j), max(c, k)
            
        return [a, b, c] == [x, y, z]