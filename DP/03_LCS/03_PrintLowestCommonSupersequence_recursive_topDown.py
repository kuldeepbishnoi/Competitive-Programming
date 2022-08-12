"""
Created on Sun Apr 17 11:53:34 2022

@author: Kuldeep
"""

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        memo = self.lcs(str1, str2, len(str1), len(str2))
        ans = ''
        i = len(str1)
        j = len(str2)
        while i != 0 and j !=0:
            if str1[i-1] == str2[j-1]:
                ans += str1[i-1]
                i-=1
                j-=1
            else:
                if memo[i-1][j]>=memo[i][j-1]:
                    ans += str1[i-1]
                    i-=1
                else:
                    ans += str2[j-1]
                    j-=1
        while i!=0:
            ans += str1[i-1]
            i-=1
            
        while j!=0:
            ans += str2[j-1] 
            j-=1
        
        return ans[::-1]
            

    def lcs(self, X, Y, m, n):
        memo = [[0 for i in range(n+1)]
                    for j in range(m+1)]
        # row -> X
        # col -> Y
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if X[i-1] == Y[j-1]:
                    memo[i][j] = memo[i-1][j-1]+1
                else:
                    memo[i][j] = max(memo[i-1][j], 
                                     memo[i][j-1])
        return memo	    
    
if __name__=='__main__':
    sol = Solution()
    str1 = 'abac'
    str2 = 'cab'
    print(sol.shortestCommonSupersequence(str1, str2))
