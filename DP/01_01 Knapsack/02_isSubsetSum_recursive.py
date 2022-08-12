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
    def solve(self, idx, S):
        if S==0:
            return True
        if idx==0 or S<0:
            return False
        
        if arr[idx-1]<=S:
            return self.solve(idx-1, S-arr[idx-1]) or\
            self.solve(idx-1, S)
        else:
            return self.solve(idx-1, S)

if __name__=='__main__':
    sol = Solution()
    arr = [3, 34, 4, 12, 5, 2]
    print(sol.isSubsetSum(len(arr), arr, 9))
