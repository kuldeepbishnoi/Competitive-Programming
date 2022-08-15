"""
Created on Thu Apr 21 08:38:54 2022

@author: Kuldeep
"""

import functools
class Solution:
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        self.memo = {}
        ans = self.solve(s1, s2)
        # for i, j in self.memo.items():
        #     print(i, j)
        return ans
    
    @functools.lru_cache(maxsize=None)
    def solve(self, s1, s2):
        if (s1, s2) in self.memo:
            return self.memo[(s1, s2)]
        if s1==s2:
            self.memo[(s1, s2)] = True
            return True
        n = len(s1)
        if n==1:
            self.memo[(s1, s2)] = False
            return False
        for k in range(1, n):
            # print('------Swapped-----')
            swapped = False
            if self.solve(s1[0:k], s2[n-k:]): 
                swapped = self.solve(s1[k:], s2[:n-k])
            if swapped:
                self.memo[(s1, s2)] = True
                return True
            # print('------Not Swapped-----')
            not_swapped = False
            if self.solve(s1[0:k], s2[0:k]):
                not_swapped = self.solve(s1[k:], s2[k:])
            if not_swapped:    
                self.memo[(s1, s2)] = True
                return True
        self.memo[(s1, s2)] = False
        return False
        
        
if __name__=='__main__':
    sol = Solution()
    # s1 = 'great'
    # s2 = 'rgeat'
    s1 = 'abcde'
    s2 = 'caebd'
    # s1= 'gr'
    # s2 = 'rg'
    print(sol.isScramble(s1, s2))
