"""
Created on Sun Apr 10 17:19:37 2022

@author: Kuldeep
"""

class Solution():
    def _01_knapsack(self,W, wt, val, n):
        
        self.W = W
        self.wt = wt
        self.val = val
        self.n = n
        self.memo = [[None for i in range(W+1)]
                         for j in range(n+1)]
        self.solve(W, n)
        return self.memo[n][W]
    
    def solve(self, w, n):
    
        #Base Condition
        if n == 0 or w == 0:
            return 0
        
        if self.memo[n][w] != None:
            return self.memo[n][w]
        
        #Choice Diagram
        if self.wt[n-1]-w >= 0:
            self.memo[n][w] =  max(self.solve(w-self.wt[n-1], n-1) + self.val[n-1],
                                   self.solve(w, n-1))
        else:
            self.memo[n][w] = self.solve(w, n-1)
        
        return self.memo[n][w]
            
if __name__=='__main__':
    wt = [4,5,1]
    val = [1,2,3]
    W = 4
    n = 3
    print(Solution()._01_knapsack(W, wt, val, n))
