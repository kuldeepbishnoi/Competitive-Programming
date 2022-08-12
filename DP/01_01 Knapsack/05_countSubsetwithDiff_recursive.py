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
        return self.solve(len(arr), S)
    
    def solve(self, idx, S):
        if S==0:
            return 1
        if S<0 or idx == 0:
            return 0
        # print(idx, S)
        if S-self.arr[idx-1]>=0:
            return self.solve(idx-1, S-self.arr[idx-1]) +\
                   self.solve(idx-1, S)
        else:
            return self.solve(idx-1, S)

if __name__=='__main__':
    sol = Solution()
    arr = [1, 1, 2, 3]
    print(sol.fun(arr, 1))
