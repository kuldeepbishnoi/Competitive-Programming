"""
Created on Wed Apr 13 20:12:59 2022

@author: Kuldeep
"""

class Solution:
    def minCoins(self, coins, M, V):
        self.coins = coins
        self.memo = [[None for i in range(1+V)]
                        for j in range(1+M)]
        ans = self.solve(M, V)
        if ans == float('inf'):
            return -1
        return ans

    def solve(self, idx, V):
        if V==0:
            return 0
        if idx==0 or V<0:
            return float('inf')
        if self.memo[idx][V] != None:
            return self.memo[idx][V]
        if V-self.coins[idx-1]>=0:
            self.memo[idx][V]=  min(1 + self.solve(idx, V-self.coins[idx-1]),
                                        self.solve(idx-1, V))
        else:
            self.memo[idx][V] = self.solve(idx-1, V)
        return self.memo[idx][V]
    
if __name__=='__main__':
    sol = Solution()
    coins = [25,10,5]
    M = len(coins)
    V = 30
    print(sol.minCoins(coins, M, V))
