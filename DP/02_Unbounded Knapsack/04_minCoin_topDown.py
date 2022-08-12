"""
Created on Wed Apr 13 20:12:59 2022

@author: Kuldeep
"""

class Solution:
    def minCoins(self, coins, M, V):
        memo = [[float('inf') for i in range(V+1)]
                                for j in range(M+1)]
        for i in range(1+M):
            memo[i][0] = 0
        
        for i in range(1, M+1):
            for j in range(1, V+1):        
                if j-coins[i-1]>=0:
                    memo[i][j]=  min(1+memo[i][j-coins[i-1]],
                                      memo[i-1][j])
                else:
                    memo[i][j] = memo[i-1][j]
        ans = memo[-1][-1]
        if ans == float('inf'):
            return -1
        return ans
    
if __name__=='__main__':
    sol = Solution()
    coins = [25,10,5]
    M = len(coins)
    V = 30
    print(sol.minCoins(coins, M, V))
