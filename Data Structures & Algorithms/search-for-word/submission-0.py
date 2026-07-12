class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, w, in_path):
            if w == "":
                return True
            if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or (i,j) in in_path or w[0] != board[i][j]:
                return False
            
            in_path[(i, j)] = 1
            b = False
            if dfs(i+1, j, w[1:], in_path) or dfs(i-1, j, w[1:], in_path) or dfs(i, j+1, w[1:], in_path) or dfs(i, j-1, w[1:], in_path):
                b = True
            
            del in_path[(i, j)]
            return b
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, word, {}):
                    return True
        
        return False