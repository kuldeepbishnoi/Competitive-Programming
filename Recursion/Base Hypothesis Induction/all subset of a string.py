"""
Created on Sat Apr 23 15:41:16 2022

@author: Kuldeep
"""

class Solution():
    def fun(self, string):
        self.ans = []
        self.string = string
        self.solve(len(string)-1, "")
        return self.ans
        
    def solve(self, n, string):
        if n==-1:
            self.ans.append(string)
            return 
        
        print(n)
        self.solve(n-1, self.string[n]+string)
        self.solve(n-1, string)
        
        
if __name__=='__main__':
    sol = Solution()
    string = "abc"
    print(sol.fun(string))
