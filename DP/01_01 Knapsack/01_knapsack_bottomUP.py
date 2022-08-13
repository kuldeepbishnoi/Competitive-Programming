"""
Created on Sun Apr 10 17:19:37 2022

@author: Kuldeep
"""

class Solution():
    def _01_knapsack(self, W, wt, val, N):
        
        memo = [[None for i in range(W+1)]
                        for j in range(N+1)]
        #Base Condition
        for n in range(N+1):
            for w in range(W+1):
                if n==0 or w==0:
                    memo[n][w] = 0
        
        #choice diagram
        for n in range(1, N+1):
            for w in range(1, W+1):
                if w-wt[n-1]>=0:
                    memo[n][w] = max(val[n-1]+memo[n-1][w-wt[n-1]],
                                     memo[n-1][w])
                else:
                    memo[n][w] = memo[n-1][w]
        
        return memo[n][w]
    
if __name__=='__main__':
    wt = [4,5,1]
    val = [1,2,3]
    W = 4
    n = 3
    print(Solution()._01_knapsack(W, wt, val, n))
