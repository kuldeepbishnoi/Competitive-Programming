"""
Created on Sat Apr 23 17:08:54 2022

@author: Kuldeep
"""

class Solution():
    def fun(self, n):
        return self.solve(n)
    
    def solve(self, n):
        if n==1:
            return 1
        return n*self.solve(n-1)

if __name__=='__main__':
    sol = Solution()
    print(sol.fun(3))
