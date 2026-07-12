class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        g = [set() for _ in range(26)]
        in_v = [0 for _ in range(26)]
        for i in range(len(words)):
            for j in words[i]:
                in_v[ord(j) - ord('a')] += 1
            if i > 0:
                b = False
                for j in range(min(len(words[i]), len(words[i-1]))):
                    if words[i-1][j] != words[i][j]:
                        g[ord(words[i-1][j]) - ord('a')].add(ord(words[i][j]) - ord('a'))
                        b = True
                        break
                if not b and len(words[i]) < len(words[i-1]):
                    return ""
        
        #print(g)
        #print(in_v)
        
        return self.topo_sort(g, in_v)
    
    def topo_sort(self, g: list[list[int]], in_v: list[int]) -> str:
        res = []
        v = [0 for _ in range(26)]
        def dfs(i, in_path):
            #print(i, in_path)
            if i in in_path:
                return False
            if v[i] == 1:
                return True
            #print(i, in_path)
            in_path[i] = 1
            v[i] = 1
            for j in g[i]:
                if not dfs(j, in_path):
                    return False
            del in_path[i]
            res.append(i)
            return True
        
        for i in range(26):
            if in_v[i] > 0:
                if not dfs(i, {}):
                    return ""
        
        for i in range(len(res)):
            res[i] = chr(ord('a') + res[i])

        return ''.join(res[::-1])






