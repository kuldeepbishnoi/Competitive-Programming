"""
Created on Wed Apr 13 09:33:17 2022

@author: Kuldeep
"""

class Solution():
    def fun(self, arr, diff):
        if (diff+sum(arr)) %2 != 0:
            return -1
        S = (diff+sum(arr))//2
        memo = [[0 for i in range(S+1)]
                         for j in range(len(arr)+1)]
        for i in range(0, len(arr)+1):
            memo[i][0] = 1
        for i in range(1, len(arr)+1):
            for j in range(1, S+1):
                if j-arr[i-1]>=0:
                    memo[i][j] = memo[i-1][j-arr[i-1]] +\
                           memo[i-1][j]
                else:
                    memo[i][j] = memo[i-1][j]
        return memo[-1][-1]
            
if __name__=='__main__':
    sol = Solution()
    arr = [1, 1, 2, 3]
    print(sol.fun(arr, 1))
