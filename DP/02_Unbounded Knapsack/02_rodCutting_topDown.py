"""
Created on Wed Apr 13 15:39:48 2022

@author: Kuldeep
"""

# import functools
class Solution:
    def cutRod(self, price, n):
        memo = [[0 for i in range(n+1)]
                       for j in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if j-i>=0:
                    memo[i][j] =  max(memo[i-1][j],
                                     price[i-1] + memo[i][j-i])
                else:
                    memo[i][j] = memo[i-1][j]                
                        
        return memo[-1][-1]
    
    # @functools.lru_cache(maxsize=None)
    def solve(self, idx, length):
        if idx==0 or length==0:
            return 0
        if self.memo[idx][length] != None:
            return self.memo[idx][length]
        return self.memo[idx][length]

if __name__=='__main__':
    sol = Solution()
    n = 8
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    print(sol.cutRod(price, n))
