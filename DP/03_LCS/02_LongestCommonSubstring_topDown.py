"""
Created on Wed Apr 13 22:24:21 2022

@author: Kuldeep
"""

class Solution:
    def longestCommonSubstr(self, s1, s2, N, M):        
        memo = [[None for i in range(M+1)]
                    for j in range(N+1)]
        ans = 0
        for n in range(N+1):
            for m in range(M+1):
                if n==0 or m==0:
                    memo[n][m] = 0
                    
        for n in range(1, N+1):
            for m in range(1, M+1):
                if s1[n-1] == s2[m-1]:
                    memo[n][m] = 1+memo[n-1][m-1]
                    ans = max(memo[n][m], ans)
                else:
                    memo[n][m] = 0
        return ans


if __name__=='__main__':
    sol = Solution()
    s1 = 'ABC'
    s2 = 'ABCD'
    print(sol.longestCommonSubstr(s1, s2 ,len(s1), len(s2)))
