"""
Created on Wed Apr 13 20:12:59 2022

@author: Kuldeep
"""

import functools
class Solution:
    def minCoins(self, coins, M, V):
        self.coins = coins
        ans = self.solve(M, V)
        if ans == float('inf'):
            return -1
        return ans
        
    @functools.lru_cache(maxsize=None)
    def solve(self, idx, V):
        if V==0:
            return 0
        if idx==0 or V<0:
            return float('inf')
        if V-self.coins[idx-1]>=0:
            return min(1 + self.solve(idx, V-self.coins[idx-1]),
                           self.solve(idx-1, V))
        else:
            return self.solve(idx-1, V)
        
if __name__=='__main__':
    sol = Solution()
    coins = [25,10,5]
    M = len(coins)
    V = 30
    print(sol.minCoins(coins, M, V))
