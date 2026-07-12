class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        s = set()

        for i in tickets:
            s.add(i[0])
            s.add(i[1])
        
        s = sorted(s)

        m = {}
        mm = {}
        k = 0
    
        for i in s:
            m[i] = k
            mm[k] = i
            k += 1
        
        #print(m)

        adj = [[] for _ in s]

        for i in tickets:
            adj[m[i[0]]].append(m[i[1]])
        

        for i in range(len(s)):
            adj[i].sort()
            print(i, mm[i], adj[i])
        
        res = []

        def dfs(root):
            res.append(root)
            if len(res) == len(tickets) + 1:
                return True
            
            if len(adj[root]) == 0:
                res.pop()
                return False
            print(root, adj[root])
            for i, v in enumerate(adj[root]):
                p = adj[root].pop(i)
                if dfs(p):
                    return True
                else:
                    print("backtracking", root, i, v, res)
                    adj[root].insert(i, v)
            
            res.pop()
            return False

        dfs(m["JFK"])

        for i in range(len(res)):
            res[i] = mm[res[i]]
        
        return res