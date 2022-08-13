"""
Created on Sun Apr 10 17:19:37 2022

@author: Kuldeep
"""

import functools
class Solution():
    def _01_knapsack(self,W, wt, val, n):
        
        self.W = W
        self.wt = wt
        self.val = val
        self.n = n
        return self.solve(W, n)
    
    functools.lru_cache(maxsize = None)
    def solve(self, w, n):
    
        #Base Condition
        if n == 0 or w == 0:
            return 0
        
        #Choice Diagram
        if w-wt[n-1] >= 0:
            return max(self.solve(w-self.wt[n-1], n-1) + self.val[n-1],
                       self.solve(w, n-1))
        else:
            return self.solve(w, n-1)
            
if __name__=='__main__':
    wt = [4,5,1]
    val = [1,2,3]
    W = 4
    n = 3
    print(Solution()._01_knapsack(W, wt, val, n))
