"""
Created on Wed Apr 20 06:00:22 2022

@author: Kuldeep
"""

import functools
class Solution:
    def countWays(self, n, s):
        self.s = s
        return self.solve(0, n-1, True)
    
    @functools.lru_cache(maxsize=None)
    def solve(self, i, j, boolean):
        if i==j:
            if boolean == True:
                return self.s[i] == 'T'
            if boolean == False:
                return self.s[i] == 'F'
            
        ans = 0
        for k in range(i+1, j, 2):
            lt = self.solve(i, k-1, True)
            lf = self.solve(i, k-1, False)
            rt = self.solve(k+1, j, True)
            rf = self.solve(k+1, j, False)
            
            if self.s[k] == '|':
                if boolean == True:
                    # TT
                    # FT
                    # TF
                    ans += lt*rt +\
                           lf*rt +\
                           lt*rf
                else:
                    # FF
                    ans += lf*rf
            elif self.s[k] == '^':
                if boolean == True:
                    #TF
                    #FT
                    ans += lt*rf +\
                           lf*rt
                else:
                    #TT
                    #FF
                    ans += lt*rt +\
                           lf*rf
            elif self.s[k] == '&':
                if boolean == True:
                    #TT
                    ans += lt*rt
                else:
                    #FF
                    #TF
                    #FT
                    ans += lf*rf +\
                           lt*rf +\
                           lf*rt
        return ans  
    
if __name__=='__main__':
    sol = Solution()
    s = 'T|T&F^T'
    print(sol.countWays(len(s), s))
