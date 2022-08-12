"""
Created on Tue Apr 12 08:52:20 2022

@author: Kuldeep
"""

import functools
class Solution:
    def perfectSum(self, arr, N, S):
        self.arr = arr
        return self.solve(N, S)
    
    @functools.lru_cache(maxsize=None)
    def solve(self, idx, S):
        # if S==0 :
        #     return 1
        # if S<0 or idx == 0:
        #     return 0
        if idx==0:
            if S==0:
                return 1
            else:
                return 0
        
        if arr[idx-1]<=S:
            return self.solve(idx-1, S-arr[idx-1]) +\
                   self.solve(idx-1, S)
        return self.solve(idx-1, S)
        
if __name__=='__main__':
    sol = Solution()
    arr = [9,7,0,3,9,8,6,5,7,6]
    print(sol.perfectSum(arr, len(arr), 31))

