"""
Created on Thu Apr 14 06:47:23 2022

@author: Kuldeep
"""

import functools
class Solution:
    def longestCommonSubstr(self, s1, s2, x, y):        
        self.s1 = s1
        self.s2 = s2
        return self.solve(len(s1), len(s2), 0)
    
    @functools.lru_cache(maxsize=None)
    def solve(self, x, y, count):
        if x==0 or y==0:
            return count
        if self.s1[x-1]==self.s2[y-1]:
            count = self.solve(x-1, y-1, count+1)
        count = max(count, self.solve(x-1, y, 0), self.solve(x, y-1, 0))
        return count
    
if __name__=='__main__':
    sol = Solution()
    s1 = 'ABCDGH'
    s2 = 'ACDGHR'
    print(sol.longestCommonSubstr(s1, s2, len(s1), len(s2)))
