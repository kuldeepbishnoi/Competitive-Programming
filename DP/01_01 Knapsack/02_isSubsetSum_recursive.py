"""
Created on Tue Apr 12 04:53:21 2022

@author: Kuldeep
"""

import functools
class Solution:
    def isSubsetSum (self, N, arr, S):
        self.arr = arr
        return self.solve(N, S)
    
    @functools.lru_cache(maxsize=None)
    def solve(self, n, S):
        #Base Condition
        if S==0:
            return True
        if n==0:
            return False
        
        #Choice Diagram
        if S-self.arr[n-1]>=0:
            return self.solve(n-1, S-self.arr[n-1]) or\
                    self.solve(n-1, S)
        else:
            return self.solve(n-1, S)

if __name__=='__main__':
    sol = Solution()
    arr = [3, 34, 4, 12, 5, 2]
    print(sol.isSubsetSum(len(arr), arr, 9))
