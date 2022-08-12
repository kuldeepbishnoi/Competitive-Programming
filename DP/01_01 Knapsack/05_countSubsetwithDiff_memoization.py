"""
Created on Wed Apr 13 09:33:17 2022

@author: Kuldeep
"""

class Solution():
    def fun(self, arr, diff):
        if (diff+sum(arr)) %2 != 0:
            return -1
        self.arr = arr
        S = (diff+sum(arr))//2
        self.memo = [[None for i in range(S+1)]
                     for j in range(len(arr)+1)]
        self.solve(len(arr), S)
        return None
    
    def solve(self, idx, S):
        if S==0:
            return 1
        if S<0 or idx == 0:
            return 0
        if self.memo[idx][S] != None:
            return self.memo[idx][S]
        # print(idx, S)
        if S-self.arr[idx-1]>=0:
            self.memo[idx][S] = self.solve(idx-1, S-self.arr[idx-1]) +\
                                   self.solve(idx-1, S)
        else:
            self.memo[idx][S] = self.solve(idx-1, S)
        return self.memo[idx][S]

if __name__=='__main__':
    sol = Solution()
    arr = [1, 1, 2, 3]
    print(sol.fun(arr, 1))
