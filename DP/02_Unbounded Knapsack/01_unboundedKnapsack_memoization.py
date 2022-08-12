"""
Created on Wed Apr 13 14:01:09 2022

@author: Kuldeep
"""

# import functools
class Solution:
    def knapSack(self, N, W, val, wt):
        self.val = val
        self.wt = wt
        self.memo = [[None for i in range(W+1)]
                            for j in range(N+1)]
        temp = max(0, self.solve(N, W))
        return temp
      
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
                                   self.val[idx-1] + self.solve(idx, W-self.wt[idx-1]))
                       
        else:
            self.memo[idx][W] = self.solve(idx-1, W)
        return self.memo[idx][W]
        
if __name__=='__main__':
    sol = Solution()
    val = [1, 4, 5, 7]
    wt = [1, 3, 4, 5]
    print(sol.knapSack(4, 8, val, wt))
