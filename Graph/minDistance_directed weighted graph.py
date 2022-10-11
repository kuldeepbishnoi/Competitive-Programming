"""
Tags:
    -
    
Time: O()
Space: O()
    
Apprach:
    Option1: Similar to 
        -
        
Problem:
    minimum in distance in weighted directed graph
    
"""
from collections import deque
class Solution():
    def minDistance(self, V, adj, src, dest):
        q = self.topoSort(V, adj)
        dist = [float('inf')]*V
        def bfs():
            while(q):
                node = q.pop()
                if dist[node]!=float('inf'):
                    for nei,w in adj[node]:
                        if dist[nei]>dist[node]+w:
                            dist[nei] = dist[node]+w
        
        dist[src] = 0
        bfs()
        print(dist)
        return dist[dest]
        
    def topoSort(self, V, adj):
        def dfs(node):
            vis[node] = True
            for i,_ in adj[node]:
                if not vis[i]:
                    dfs(i)
            ans.append(node)
        ans = deque()
        vis = [False] * V
        for i in range(V):
            if not vis[i]:
                dfs(i)
        return ans

if __name__=='__main__':
    sol = Solution()
    V = 6
    adj = [[[1,2],[4,1]],
           [[2,3]],
           [[3,6]],
           [],
           [[2,2],[5,4]],
           [[3,1]]]
    print(sol.minDistance(V, adj, 0, 3))
