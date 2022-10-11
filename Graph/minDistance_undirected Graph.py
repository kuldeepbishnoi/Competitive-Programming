from collections import deque
class Solution:
    def minDistance(self, V, adj, src, dest):
        dist = [float('inf')]*V
        def bfs(node):
            q = deque()
            q.append(node)
            while(q):
                node = q.pop()
                for nei in adj[node]:
                    if dist[nei]>dist[node]+1:
                       dist[nei] = dist[node]+1
                       q.append(nei)
        dist[src]=0
        bfs(src)
        print(dist)
        return dist[dest]
        

if __name__ == '__main__':
    V = 4
    adj = [[1,3],[0,2],[1,3],[0,2]]
    # 0-1
    # | |
    # 3-2
    sol = Solution()
    print(sol.minDistance(V, adj, 0, 2))