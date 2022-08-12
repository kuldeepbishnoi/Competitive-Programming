"""
Created on Wed Apr 13 10:23:17 2022

@author: Kuldeep
"""

import functools
class Solution:
    def findTargetSumWays(self, arr, N, target):
        self.arr = arr
        # self.S = 0
        # for i in arr:
        #     self.S += abs(i)
        # self.memo = [[0 for i in range(2*self.S + 10)]
        #                    for j in range(N+1)]
        # self.minTarget = float('inf')
        # self.maxTarget = float('-inf')
        return self.solve(N, target)
        # print(self.minTarget, self.maxTarget)
    
    @functools.lru_cache(maxsize=None)
    def solve(self, N, target):
        if N==0:
            if target==0:
                return 1
            else:
                return 0
        # self.minTarget = min(self.minTarget, target)
        # self.maxTarget = max(self.maxTarget, target)
        # print(N, target, target+self.S)
        # if self.memo[N][target+self.S] != 0:
        #     return self.memo[N][target+self.S+1]
        return self.solve(N-1, target-self.arr[N-1]) +\
                                self.solve(N-1, target+self.arr[N-1])
        # return self.memo[N][target+self.S]

if __name__=='__main__':
    sol = Solution()
    arr = [1, 1, 1, 1, 1]
    print(sol.findTargetSumWays(arr, len(arr), 3))
