"""
Created on Wed Apr 13 22:24:21 2022

@author: Kuldeep
"""

class Solution:
    def lcs(self,x,y,s1,s2):
        memo = [[0 for i in range(x+1)]
                    for j in range(y+1)]
        for i in range(1, y+1):
            for j in range(1, x+1):
                if s2[i-1] == s1[j-1]:
                    memo[i][j] = 1+memo[i-1][j-1]
                else:
                    # print(i, j)
                    memo[i][j] = max(memo[i-1][j],
                                     memo[i][j-1])
        return memo[-1][-1]
    
    # @functools.lru_cache(maxsize=None)
    # def solve(self, x, y):
    #     if x==0 or y==0:
    #         return 0
        
    #     if self.s1[x-1] == self.s2[y-1]:
    #         return 1+self.solve(x-1, y-1)
    #     else:
    #         return max(self.solve(x-1, y),
    #                    self.solve(x, y-1))
            
if __name__=='__main__':
    sol = Solution()
    s1 = 'ABC'
    s2 = 'ABCD'
    print(sol.lcs(len(s1), len(s2), s1, s2))
