class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        lo = 0
        hi = m * n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            r = mid // n
            c = mid % n
            print(lo, hi, mid)
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return False