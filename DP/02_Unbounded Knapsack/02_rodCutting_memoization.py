"""
Created on Wed Apr 13 15:39:48 2022

@author: Kuldeep
"""

# import functools
class Solution:
    def cutRod(self, price, n):
        self.price = price
        self.memo = [[None for i in range(n+1)]
                             for j in range(n+1)]
        return self.solve(n, n)
    
    # @functools.lru_cache(maxsize=None)
    def solve(self, idx, length):
        if idx==0 or length==0:
            return 0
        if self.memo[idx][length] != None:
            return self.memo[idx][length]
        if length-idx>=0:
            self.memo[idx][length] =  max(self.solve(idx-1, length),
                                          self.price[idx-1] + self.solve(idx, length-idx))
        else:
            self.memo[idx][length] = self.solve(idx-1, length)                
        return self.memo[idx][length]

if __name__=='__main__':
    sol = Solution()
    n = 8
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    print(sol.cutRod(price, n))
