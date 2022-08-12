"""
Created on Wed Apr 13 15:39:48 2022

@author: Kuldeep
"""

import functools
class Solution:
    def cutRod(self, price, n):
        self.price = price
        return self.solve(n, n)
    
    @functools.lru_cache(maxsize=None)
    def solve(self, idx, length):
        if idx==0 or length==0:
            return 0
        if length-idx>=0:
            return max(self.solve(idx-1, length),
                        self.price[idx-1] + self.solve(idx, length-idx))
        else:
            return self.solve(idx-1, length)                


if __name__=='__main__':
    sol = Solution()
    n = 8
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    print(sol.cutRod(price, n))
