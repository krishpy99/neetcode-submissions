class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [None] * n
        for i in edges:
            if adj[i[0]] is None:
                adj[i[0]] = []
            if adj[i[1]] is None:
                adj[i[1]] = []
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        
        v = [0] * n

        flag = True
        cnt = 0

        def dfs(root, parent):
            nonlocal flag, cnt
            v[root] = 1
            cnt += 1
            print(root, "->")
            if adj[root] is None:
                return
            for i in adj[root]:
                if i != parent and v[i] == 1 or i == root:
                    flag = False
                    return
                if i != parent:
                    dfs(i, root)
        
        dfs(0, 0)

        if cnt != n:
            return False
        
        return flag
                