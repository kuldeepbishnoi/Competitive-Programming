# import functools
class Solution:
    def shortestCommonSupersequence(self, X, Y, m, n):
        # self.X = X
        # self.Y = Y
        return m+n-self.lcs(X, Y, m, n)
        # return m+n-self.solve(m, n)
    
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
        return memo[m][n]

    # @functools.lru_cache(maxsize=None)
    # def solve(self, m, n):
    #     if m==0 or n==0:
    #         return 0
    #     if self.X[m-1]==self.Y[n-1]:
    #         return 1+self.solve(m-1, n-1)
    #     else:
    #         return max(self.solve(m-1, n),
    #                   self.solve(m, n-1))
