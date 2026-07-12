class Node:
    def __init__(self, c, isEnd = False):
        self.char = c
        self.next = []
        self.isEnd = isEnd

def add_word(root, word):
    if root is None:
        return
    if word == "" or word is None:
        root.isEnd = True
        return
    #print(word)
    for i in root.next:
        if i.char == word[0]:
            add_word(i, word[1:])
            return
    
    root.next.append(Node(word[0]))
    add_word(root.next[-1], word[1:])

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root1 = Node('/')
        for word in words:
            add_word(root1, word)
        
        res = set()
        def dfs(i, j, root, word, in_path):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or (i, j) in in_path:
                return
            temp = None
            for t in root.next:
                if t.char == board[i][j]:
                    temp = t
                    break
            if temp is None:
                return
            #print(root, word)
            if temp.isEnd:
                res.add(word + board[i][j])
            in_path[(i,j)] = 1
            dfs(i+1, j, temp, word + board[i][j], in_path)
            dfs(i-1, j, temp, word + board[i][j], in_path)
            dfs(i, j+1, temp, word + board[i][j], in_path)
            dfs(i, j-1, temp, word + board[i][j], in_path)
            del in_path[(i,j)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root1, "", {})
        
        return list(res)

            

