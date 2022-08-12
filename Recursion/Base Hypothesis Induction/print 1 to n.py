"""
Created on Sat Apr 23 16:55:26 2022

@author: Kuldeep
"""

class Solution():
    def fun(self, n):
        self.solve(n)
    
    def solve(self, n):
        if n==0:
            return 
        self.solve(n-1)
        print(n)
        

if __name__=='__main__':
    sol = Solution()
    n = 6
    sol.fun(n)
