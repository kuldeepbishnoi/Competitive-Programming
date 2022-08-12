"""
Created on Fri Apr 22 06:25:40 2022

@author: Kuldeep
"""

class Solution():
    def eggDrop(self, e, f):
        self.memo = [[None for i in range(f+1)]
                           for j in range(e+1)]
        return self.solve(e, f)
    
    def solve(self, e, f):
        # print(e, f)
        if f<=1:
            return f
        if e==1:
            return f
        if self.memo[e][f] != None:
            return self.memo[e][f] 
        ans = float('inf')
        for k in range(1, f+1):
            if self.memo[e-1][k-1] != None:
                broken = self.memo[e-1][k-1]
            else:
                broken = self.solve(e-1, k-1)
            # we won't check again @ k therefore f-k
            if self.memo[e][f-k] != None:
                not_broken = self.memo[e][f-k]
            else:
                not_broken = self.solve(e, f-k)
            ans = min(1 + max(broken, not_broken), ans)
        return ans

if __name__=='__main__':
    sol = Solution()
    f = 2
    e = 1
    print(sol.eggDrop(e, f))
