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
        # if in array there is 0 this can give error!!
        # if S==0 :
        #     return 1
        # if idx == 0:
        #     return 0
        if idx==0:
            if S==0:
                return 1
            else:
                return 0
        
        if S-arr[idx-1]>=0:
            return self.solve(idx-1, S-arr[idx-1]) +\
                   self.solve(idx-1, S)
        return self.solve(idx-1, S)
        
if __name__=='__main__':
    sol = Solution()
    arr = [2, 3, 5, 6, 8, 10]
    print( sol.perfectSum(arr, len(arr), 10) )

