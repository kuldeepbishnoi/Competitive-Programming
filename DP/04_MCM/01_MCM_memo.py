"""
Created on Sun Apr 17 18:23:40 2022

@author: Kuldeep
"""

import functools
class Solution:
    def matrixMultiplication(self, N, arr):
        self.arr = arr
        self.memo = [[None for i in range(N)]
                             for j in range(N)]
        temp = self.solve(1, N-1)
        for i in self.memo:
            print(i)
        return temp
    
    @functools.lru_cache(maxsize=None)
    def solve(self, i, j):
        if i==j:
            return 0
        if self.memo[i][j] != None:
            return self.memo[i][j]
        ans = float('inf')
        for k in range(i, j):
            ans = min(ans, self.solve(i, k) + self.solve(k+1, j) +
                           self.arr[i-1]*self.arr[j]*self.arr[k])
        self.memo[i][j] = ans
        return ans
    
if __name__=='__main__':
    sol = Solution()
    arr = [40, 20, 30, 10, 30]
    print(sol.matrixMultiplication(len(arr), arr))
