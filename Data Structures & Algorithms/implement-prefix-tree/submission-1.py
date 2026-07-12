class Node:
    
    def __init__(self, ch = ""):
        self.end = False
        self.next = [None] * 26

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        temp = self.root
        for ch in word:
            if temp.next[ord(ch) - ord('a')] is None:
                temp.next[ord(ch) - ord('a')] = Node()
            temp = temp.next[ord(ch) - ord('a')]
        
        temp.end = True

    def search(self, word: str) -> bool:
        temp = self.root
        for ch in word:
            temp = temp.next[ord(ch) - ord('a')]
            if temp is None:
                return False
        
        return temp.end

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for ch in prefix:
            temp = temp.next[ord(ch) - ord('a')]
            if temp is None:
                return False
        
        return True
        