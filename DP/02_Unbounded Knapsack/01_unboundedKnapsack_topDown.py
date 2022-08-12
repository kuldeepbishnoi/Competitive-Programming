"""
Created on Wed Apr 13 14:01:09 2022

@author: Kuldeep
"""

# import functools
class Solution:
    def knapSack(self, N, W, val, wt):
        memo = [[0 for i in range(W+1)]
                              for j in range(N+1)]
        
        for i in range(1, N+1):
            for j in range(1, W+1):
                if j-wt[i-1]>=0:
                    memo[i][j] = max(memo[i-1][j],
                                     val[i-1] + memo[i][j-wt[i-1]])
                               
                else:
                    memo[i][j] = memo[i-1][j]
                 
        return memo[-1][-1]
    
    # @functools.lru_cache(maxsize=None)
    def solve(self, idx, W):
        if W==0:
            return 0
        if idx==0 or W<0:
            return float('-inf')
        if self.memo[idx][W] != None:
            return self.memo[idx][W]
        if W-self.wt[idx-1]>=0:
            self.memo[idx][W] = max(self.solve(idx-1, W),
                                   self.val[idx-1] + self.solve(idx-1, W-self.wt[idx-1]),
                                   self.val[idx-1] + self.solve(idx, W-self.wt[idx-1]))
                       
        else:
            self.memo[idx][W] = self.solve(idx-1, W)
        return self.memo[idx][W]
        
if __name__=='__main__':
    sol = Solution()
    val = [1, 4, 5, 7]
    wt = [1, 3, 4, 5]
    print(sol.knapSack(4, 8, val, wt))
