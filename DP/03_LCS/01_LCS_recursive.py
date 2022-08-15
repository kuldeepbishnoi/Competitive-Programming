"""
Created on Wed Apr 13 22:24:21 2022

@author: Kuldeep
"""

import functools
class Solution:
    def lcs(self, n, m, s1, s2):
        self.s1 = s1
        self.s2 = s2
        return self.solve(n, m)
    
    @functools.lru_cache(maxsize=None)
    def solve(self, n, m):
        #Base Condition
        if n==0 or m==0:
            return 0
        
        #Choice Diagram
        if self.s1[n-1] != self.s2[m-1]:
            return max(self.solve(n-1, m),
                       self.solve(n, m-1))
        else:
            return 1+self.solve(n-1, m-1)
        
        
if __name__=='__main__':
    sol = Solution()
    s1 = 'ABC'
    s2 = 'ABCD'
    print(sol.lcs(len(s1), len(s2), s1, s2))
