class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        target = None
        adj = [[] for _ in range(len(wordList) + 1)]

        for i in range(len(wordList)):
            if wordList[i] == endWord:
                target = i + 1
            ch = 0
            for k in range(len(wordList[i])):
                if beginWord[k] != wordList[i][k]:
                    ch += 1
            
            if ch == 1:
                adj[0].append(i+1)
                adj[i+1].append(0)
            for j in range(i+1,len(wordList)):
                ch = 0
                for k in range(len(wordList[j])):
                    if wordList[i][k] != wordList[j][k]:
                        ch += 1
                
                if ch == 1:
                    adj[i+1].append(j+1)
                    adj[j+1].append(i+1)
        

        q = []

        v = [0 for _ in range(len(adj))]

        v[0] = 1

        for i in adj[0]:
            q.append([i, 1])
        

        cur = 0

        while len(q) - cur > 0:
            curr = q[cur]
            if curr[0] == target:
                return curr[1] + 1
            
            v[curr[0]] = 1
            for i in adj[curr[0]]:
                if v[i] == 0:
                    q.append([i, curr[1] + 1])
            
            cur += 1
        
        return 0