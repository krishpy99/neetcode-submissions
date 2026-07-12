class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # subbox
        sb = {}
        # rows & cols
        for i in range(9):
            r, l = [], []
            for j in range(9):
                if board[i][j].isnumeric():
                    r.append(board[i][j])
                    p = (i//3) * 3 + (j//3)
                    if p in sb:
                        sb[p].append(board[i][j])
                    else:
                        sb[p] = [board[i][j]]
                if board[j][i].isnumeric():
                    l.append(board[j][i])
            rs, ls = set(r), set(l)
            if len(ls) < len(l): 
                return False
            if len(rs) < len(r): 
                return False
        
        # small boxes
        print(sb)
        for i in range(9):
            if i not in sb:
                continue
            sbs = set(sb[i])
            if len(sb[i]) > len(sbs):
                return False

        return True
            