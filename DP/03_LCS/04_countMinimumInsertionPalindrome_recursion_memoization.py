"""
Created on Sun Apr 17 13:07:53 2022

@author: Kuldeep
"""

import functools
class Solution:
    def countMin(self, S):
        return len(S)-self.longestPalin(S)
        
    def longestPalin(self, S):
        self.s1 = S
        self.s2 = S[::-1]
        return self.solve(len(S), len(S))
        
    def solve(self, x, y):
        if x==0 or y==0:
            return 0
        if self.s1[x-1]==self.s2[y-1]:
            return 1+self.solve(x-1, y-1)
        else:
            return max(self.solve(x, y-1),
                       self.solve(x-1, y))

if __name__=='__main__':
    sol = Solution()
    S = "abcd"
    print(sol.countMin(S))
