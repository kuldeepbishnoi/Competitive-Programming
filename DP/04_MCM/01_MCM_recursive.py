"""
Created on Sun Apr 17 18:23:40 2022

@author: Kuldeep
"""

import functools
class Solution:
    def matrixMultiplication(self, N, arr):
        self.arr = arr
        return self.solve(1, N-1)
    
    @functools.lru_cache(maxsize=None)
    def solve(self, i, j):
        if i==j:
            return 0
        ans = float('inf')
        for k in range(i, j):
            ans = min(ans, self.solve(i, k) + self.solve(k+1, j) +
                           self.arr[i-1]*self.arr[j]*self.arr[k])
        return ans
    
if __name__=='__main__':
    sol = Solution()
    arr = [40, 20, 30, 10, 30]
    print(sol.matrixMultiplication(len(arr), arr))
