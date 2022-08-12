"""
Created on Wed Apr 13 22:24:21 2022

@author: Kuldeep
"""

class Solution:
    def longestCommonSubstr(self, s1, s2, x, y):        
        memo = [[0 for i in range(x+1)]
                    for j in range(y+1)]
        ans = 0
        for i in range(1, y+1):
            for j in range(1, x+1):
                if s2[i-1] == s1[j-1]:
                    memo[i][j] = 1+memo[i-1][j-1]
                    ans = max(memo[i][j], ans)
                else:
                    # print(i, j)
                    memo[i][j] = 0
        # print(memo[-1][-1])
        return ans
            
if __name__=='__main__':
    sol = Solution()
    s1 = 'ABC'
    s2 = 'ABCD'
    print(sol.longestCommonSubstr(s1, s2 ,len(s1), len(s2)))
