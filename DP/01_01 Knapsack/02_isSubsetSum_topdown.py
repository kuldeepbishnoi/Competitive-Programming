"""
Created on Tue Apr 12 04:53:21 2022

@author: Kuldeep
"""

class Solution:
    def isSubsetSum (self, N, arr, S):
        memo = [[False for i in range(S+1)]
                        for j in range(N+1)]
        
        for i in range(0, N+1):
            memo[i][0] = True
        
        for n in range(1, N+1):
            for s in range(1, S+1):
                if s-arr[n-1]>=0:
                    memo[n][s] = memo[n-1][s-arr[n-1]] or\
                                memo[n-1][s]
                else:
                    memo[n][s] = memo[n-1][s]
        
        return memo[-1][-1]
    
    
if __name__=='__main__':
    sol = Solution()
    arr = [3, 34, 4, 12, 5, 2]
    print(sol.isSubsetSum(len(arr), arr, 9))
