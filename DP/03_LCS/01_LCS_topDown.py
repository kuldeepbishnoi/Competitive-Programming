"""
Created on Wed Apr 13 22:24:21 2022

@author: Kuldeep
"""

class Solution:
    def lcs(self, N, M, s1, s2):
        memo = [[None for m in range(M+1)]
                        for n in range(N+1)]
        
        #Base Condition
        for n in range(N+1):
            for m in range(M+1):
                if n==0 or m==0:
                    memo[n][m]=0
                    
        #Choice Diagram
        for n in range(1, N+1):
            for m in range(1, M+1):        
                if s1[n-1] != s2[m-1]:
                    memo[n][m] = max(memo[n-1][m],
                                     memo[n][m-1])
                else:
                    memo[n][m] = 1+memo[n-1][m-1]
        return memo[-1][-1]


        
if __name__=='__main__':
    sol = Solution()
    s1 = 'ABC'
    s2 = 'ABCD'
    print(sol.lcs(len(s1), len(s2), s1, s2))
