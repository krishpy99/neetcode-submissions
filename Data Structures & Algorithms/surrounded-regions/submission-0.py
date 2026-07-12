class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        v = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or v[i][j] or board[i][j] == "X":
                return
            v[i][j] = 1
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1:
                    if board[i][j] == "O" and v[i][j] == 0:
                        dfs(i, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if v[i][j] == 0 and board[i][j] == "O":
                    board[i][j] = "X"