class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # eleind = rowind * col + colind
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n - 1

        while l <= r:
            mid = (l + r)//2
            print(l, r, mid)
            row_index, col_index = 0, 0
            row_index = mid // n
            col_index = mid % n
            if matrix[row_index][col_index] == target:
                return True
            elif matrix[row_index][col_index] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False