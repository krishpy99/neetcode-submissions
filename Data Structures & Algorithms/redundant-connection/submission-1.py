class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in edges]

        for [i, j] in edges:
            adj[i-1].append(j-1)
            adj[j-1].append(i-1)
        
        v = [0 for _ in edges]
        d = [0 for _ in edges]

        cycle = {}

        def dfs(i, p):
            if v[i] == 1:
                return i
            x = None
            v[i] = 1
            d[i] = 1
            for j in adj[i]:
                if j != p:
                    print("enter", i, j)
                    y = dfs(j, i)
                    print("exit", i, j, y)
                    if y is not None and d[y]:
                        cycle[(i, j)] = 1
                        cycle[(j, i)] = 1
                        print("setting x for", i, "as", y)
                        x = y
            d[i] = 0
            print("x:", x, "for", i)
            return x            

        for i in range(len(edges)):
            if not v[i]:
                dfs(i, -1)
        
        print(cycle)
        for i in range(len(edges) - 1, -1, -1):
            if (edges[i][0] - 1, edges[i][1] - 1) in cycle:
                return edges[i]
        
        return None
