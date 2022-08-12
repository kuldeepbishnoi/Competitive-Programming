"""
Created on Sat Apr 23 19:07:56 2022

@author: Kuldeep
"""

class Solution:
    def kthGrammar(self, n, k):
        self.memo = [[0]]
        self.n = n
        self.solve(0)
        for row in self.memo:
            print(row)
        return self.memo[n-1][k-1]
        # print(self.memo)
    
    def solve(self, n):
        if n==self.n-1:
            return
        
        #Hypothesis/ Induction
        temp = []
        for i in self.memo[n]:
            if i==0:
                temp.extend([0, 1])
            if i==1:
                temp.extend([1, 0])
        self.memo.append(temp)
        self.solve(n+1)
        
if __name__=='__main__':
    sol = Solution()
    print(sol.kthGrammar(4, 2))
