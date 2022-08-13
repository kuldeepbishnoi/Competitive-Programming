"""
Created on Tue Apr 12 06:03:14 2022

@author: Kuldeep
"""

class Solution:
    def equalPartition(self, N, arr):
        if sum(arr)%2 != 0:
            return False
        
        self.memo = [[None for i in range(sum(arr)//2+1)]
                           for j in range(N+1)]
        self.arr = arr
        return self.solve(N, sum(arr)//2)
    
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
    print(sol.equalPartition(len(arr), arr))

