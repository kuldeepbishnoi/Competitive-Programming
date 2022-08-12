"""
Created on Wed Apr 13 22:24:21 2022

@author: Kuldeep
"""

import functools
class Solution:
    def longestRepeatingSubsequence(self,x, s):
        self.s1 = s
        self.s2 = s
        print(self.topDown(x, s))
        print(self.solve(x, x))
        print(self.solvePrint(x, x))
        
    
    def topDown(self, x, s):
        memo = [[0 for i in range(x+1)]
                    for j in range(x+1)]
        for i in range(1, x+1):
            for j in range(1, x+1):
                if s[i-1] == s[j-1] and i!=j:
                    memo[i][j] = 1+memo[i-1][j-1]
                else:
                    # print(i, j)
                    memo[i][j] = max(memo[i-1][j],
                                      memo[i][j-1])
        return memo[-1][-1]
    
    @functools.lru_cache(maxsize=None)
    def solvePrint(self, x, y):
        if x==0 or y==0:
            return ''
           
        if x==y:
            return self.solvePrint(x, y-1)
        
        if self.s1[x-1] == self.s2[y-1]:
            return self.solvePrint(x-1, y-1) + self.s1[x-1]
           
        else:
            candidate1 = self.solvePrint(x-1, y)
            candidate2 = self.solvePrint(x, y-1)
            if len(candidate1) > len(candidate2):
                return candidate1
            else:
                return candidate2
           
    @functools.lru_cache(maxsize=None)
    def solve(self, x, y):
        if x==0 or y==0:
            return 0
        
        if x==y:
            return self.solve(x, y-1)
        
        if self.s1[x-1] == self.s2[y-1]:
            return 1+self.solve(x-1, y-1)
        else:
            return max(self.solve(x-1, y),
                        self.solve(x, y-1))
            # 
if __name__=='__main__':
    sol = Solution()
    s = 'AABEBCDD'
    sol.longestRepeatingSubsequence(len(s), s)
