class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        assert n == len(matrix[0])
        def rot(a, b, c, d):
            return d, a, b, c
        for i in range(0, n):
            for j in range(i, n - i - 1):
                matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i] = rot(matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i])
                print(rot(matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i]))
