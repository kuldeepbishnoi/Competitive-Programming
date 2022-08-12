"""
Created on Tue Apr 12 04:53:21 2022

@author: Kuldeep
"""

class Solution:
    def equalPartition (self, N, arr):
        if sum(arr)%2 != 0:
            return False
        
        S = sum(arr)//2
        
        memo = [[False for i in range(S+1)]
                for j in range(N+1)]
        
        for i in range(0, N+1):
            memo[i][0] = True
        
        for i in range(1, N+1):
            for j in range(1, S+1):
                if arr[i-1]<=j:
                    memo[i][j] = memo[i-1][j-arr[i-1]] or\
                                memo[i-1][j]
                if arr[i-1]>j:
                    memo[i][j] = memo[i-1][j]
        
        return memo[-1][-1]

if __name__=='__main__':
    sol = Solution()
    arr = [3, 34, 4, 12, 5, 2]
    print(sol.equalPartition(len(arr), arr))
    
