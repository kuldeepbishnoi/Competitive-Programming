"""
Created on Wed Apr 13 17:10:02 2022

@author: Kuldeep
"""
class Solution:
    def count(self, S, m, n):
        self.S = S
        self.memo = [[None for i in range(n+1)]
                     for j in range(m+1)]
        return self.solve(m, n)
    
    def solve(self, idx, money):
        if money==0:
            return 1
        if idx==0 or money<0:
            return 0
        
        if self.memo[idx][money] != None:
            return self.memo[idx][money]
        
        if money-self.S[idx-1]>=0:
            self.memo[idx][money] = self.solve(idx-1, money)+\
                                    self.solve(idx, money-self.S[idx-1])
        else:
            self.memo[idx][money] = self.solve(idx-1, money)
        return self.memo[idx][money]

if __name__=='__main__':
    sol = Solution()
    S = [1,2,3]
    m = len(S)
    n = 4
    print(sol.count(S, m, n))
