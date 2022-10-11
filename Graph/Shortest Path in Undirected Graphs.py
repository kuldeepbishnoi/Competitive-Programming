"""
Tags:
    -Graph
    -Dijkstra's Algorithm
    
Time: O(N+E + Nlogn) #it's make sure that we traverse no more 
Space: O()
    
Apprach:
    Option1: Similar to 
        -
        
Problem:
    
    
"""
from sortedcontainers import SortedList
class Solution():
    def minDistance(self, V, adj, src):
        #item -> [node, dist]
        h = SortedList(key= lambda item: -item[1])
        def bfs(src):
            h.add([src, 0])
            vis[0] = True
            while(h):
                node,_ = h.pop()
                for nei, w in adj[node]:
                    if not vis[nei] and dist[nei]>dist[node]+w:
                        vis[nei] = True
                        dist[nei] = dist[node]+w
                        h.add([nei, dist[nei]])
        dist = [float('inf')]*V
        vis = [False]*V #to overcome addition of node again in h
        dist[src] = 0
        bfs(0)
        return dist

if __name__=='__main__':
    sol = Solution()
    V = 5
    adj = [[[1,2],[3,1]],
           [[0,2],[4,5],[2,4]],
           [[1,4],[3,3],[4,1]],
           [[0,1],[2,3]],
           [[1,5],[2,1]]]
    print(sol.minDistance(V, adj, 0))
