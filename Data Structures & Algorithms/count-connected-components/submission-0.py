class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        
        cnt = 0

        v = [0] * n
        def dfs(root):
            v[root] = 1
            for i in adj[root]:
                if v[i] == 0:
                    dfs(i)
            
        cnt = 0
        print(adj)
        for i in range(n):
            if v[i] == 0:
                cnt += 1
                dfs(i)
                print(i, v)
        
        return cnt