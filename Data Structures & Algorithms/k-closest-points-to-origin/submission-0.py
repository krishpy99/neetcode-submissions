class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []

        for i in points:
            ans.append([(i[0] * i[0] + i[1] * i[1]) ** 0.5, i[0], i[1]])
        
        ans.sort()
        ans = ans[::-1]

        res = []
        while k > 0:
            k -= 1
            res.append([ans[-1][1], ans[-1][2]])
            ans.pop()
        
        return res