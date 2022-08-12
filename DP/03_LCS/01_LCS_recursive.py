"""
Created on Wed Apr 13 22:24:21 2022

@author: Kuldeep
"""

import functools
class Solution:
    def lcs(self,x,y,s1,s2):
        self.s1 = s1
        self.s2 = s2
        return self.solve(y, x)
    
    # @functools.lru_cache(maxsize=None)
    def solve(self, idx, till):
        if idx==0 or till<=0:
            return 0
        # print(idx, till)
        newTill = self.s1[:till].rfind(self.s2[idx-1])
        
        if newTill != -1:
            # print('hello')
            return max(self.solve(idx-1, till),
                    1+self.solve(idx-1, newTill))
        else:
            return self.solve(idx-1, till)            
            
if __name__=='__main__':
    sol = Solution()
    s1 = 'ABC'
    s2 = 'ABCD'
    print(sol.lcs(len(s1), len(s2), s1, s2))
