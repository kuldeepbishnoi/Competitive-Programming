"""
Created on Tue Apr 12 04:53:21 2022

@author: Kuldeep
"""

class Solution:
    def isSubsetSum(self, N, arr, S):
        self.arr = arr
        self.memo = [[None for i in range(S+1)]
                           for j in range(N+1)]
        return self.solve(N, S)
    
    def solve(self, idx, S):
        if S==0:
            return True
        if idx==0 or S<0:
            return False
         
        if self.memo[idx][S] != None:
            return self.memo[idx][S]
        
        if arr[idx-1]<=S:
            self.memo[idx][S] = self.solve(idx-1, S-arr[idx-1]) or\
                                self.solve(idx-1, S)
            return self.memo[idx][S]
        else:
            self.memo[idx][S] = self.solve(idx-1, S)
            return self.memo[idx][S]
        
        
if __name__=='__main__':
    sol = Solution()
    arr = [3, 34, 4, 12, 5, 2]
    print(sol.isSubsetSum(len(arr), arr, 30))
