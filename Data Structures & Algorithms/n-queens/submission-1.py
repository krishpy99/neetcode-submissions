def in_limit(i, j, n): 
    if i >= 0 and j >= 0 and i < n and j < n:
        return True
    return False

def check(board, i, j, ii, jj, n):
    while in_limit(i, j, n):
        if board[i][j] == "Q":
            return True
        i += ii
        j += jj
    return False

def verify(board, qs, n):
    for [i,j] in qs:
        if check(board, i+1, j-1, +1, -1, n):
            return False
        if check(board, i+1, j+1, +1, +1, n):
            return False
        if check(board, i-1, j-1, -1, -1, n):
            return False
        if check(board, i-1, j+1, -1, +1, n):
            return False

    return True

ans = None

def rec_place(x, n, board, rows, cols, qs, i):
    if x == 0:
        tmp = []
        for i in board:
            tmp.append(''.join(i))
        
        #print(tmp, rows, cols)
        ans.add(tuple(tmp))
        return
    
    for j in range(n):
        if cols[j] == 0 and board[i][j] != "Q":
            board[i][j] = "Q"
            rows[i] += 1
            cols[j] += 1
            qs.append([i, j])
            if verify(board, qs, n):
                rec_place(x-1, n, board, rows, cols, qs, i+1)
            qs.pop()
            rows[i] -= 1
            cols[j] -= 1
            board[i][j] = "."

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        rows = [0 for _ in range(n)]
        cols = [0 for _ in range(n)]
        qs = []
        global ans
        ans = set()

        rec_place(n, n, board, rows, cols, qs, 0)
        ans = list(ans)
        return [list(i) for i in ans]
        