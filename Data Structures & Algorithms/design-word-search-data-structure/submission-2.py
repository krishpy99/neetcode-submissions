class Node:
    def __init__(self, c = '', isEnd = False):
        self.char = c
        self.isEnd = isEnd
        self.next = [None for _ in range(26)]

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        temp = self.root
        for ch in word:
            if temp.next[ord(ch) - ord('a')] is None:
                temp.next[ord(ch) - ord('a')] = Node(ch)
            temp = temp.next[ord(ch) - ord('a')]
        temp.isEnd = True

    def look(self, word, root) -> bool:
        if len(word) == 1:
            if (word[0] == root.char or word[0] == '.') and root.isEnd:
                return True
            else:
                return False
        
        if word[0] != root.char and word[0] != '.':
            return False

        for i in root.next:
            if i is not None:
                b = self.look(word[1:], i)
                if b:
                    return True
        
        return False


    def search(self, word: str) -> bool:
        for i in self.root.next:
            if i is not None and self.look(word, i):
                return True
            
        return False