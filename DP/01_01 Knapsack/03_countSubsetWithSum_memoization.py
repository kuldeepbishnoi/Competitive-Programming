

class Solution:
    def perfectSum(self, arr, N, S):
        self.arr = arr
        self.memo = [[None for i in range(S+1)]
                           for j in range(N+1)]
        return self.solve(N, S)%(10**9 + 7)
    
    def solve(self, idx, S):
        # because here 0 is also included
        if idx==0:
            if S==0:
                return 1
            else:
                return 0
        
        if self.memo[idx][S] != None:
            return self.memo[idx][S]
        
        if S-arr[idx-1]>=0:
            self.memo[idx][S] = self.solve(idx-1, S-arr[idx-1]) +\
                                    self.solve(idx-1, S)
        else:
            self.memo[idx][S] = self.solve(idx-1, S)
        return self.memo[idx][S]

if __name__=='__main__':
    sol = Solution()
    arr = [9,7,0,3,9,8,6,5,7,6]
    print(sol.perfectSum(arr, len(arr), 31))
    
    