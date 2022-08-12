"""
Created on Wed Apr 13 17:10:02 2022

@author: Kuldeep
"""
import functools
class Solution:
    def count(self, S, m, n):
        self.S = S
        return self.solve(m, n)
    @functools.lru_cache(maxsize=None)
    def solve(self, idx, money):
        if money==0:
            return 1
        if idx==0 or money<0:
            return 0
        
        if money-self.S[idx-1]>=0:
            return self.solve(idx-1, money)+\
                    self.solve(idx, money-self.S[idx-1])
        else:
            return self.solve(idx-1, money)
        
if __name__=='__main__':
    sol = Solution()
    S = [1,2,3]
    m = len(S)
    n = 4
    print(sol.count(S, m, n))
