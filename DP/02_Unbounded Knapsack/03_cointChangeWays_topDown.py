"""
Created on Wed Apr 13 17:10:02 2022

@author: Kuldeep
"""
class Solution:
    def count(self, S, m, n):
        memo = [[0 for i in range(n+1)]
                     for j in range(m+1)]
        for i in range(0, m+1):
            memo[i][0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if j-S[i-1]>=0:
                    memo[i][j] = memo[i-1][j]+\
                                memo[i][j-S[i-1]]
                else:
                    memo[i][j] = memo[i-1][j]
                        
        return memo[-1][-1]
    
    def solve(self, idx, money):
        if money==0:
            return 1
        if idx==0 or money<0:
            return 0
        
        if self.memo[idx][money] != None:
            return self.memo[idx][money]
        
        return self.memo[idx][money]

if __name__=='__main__':
    sol = Solution()
    S = [1,2,3]
    m = len(S)
    n = 4
    print(sol.count(S, m, n))
