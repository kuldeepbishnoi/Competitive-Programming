
class Solution():
    def eggDrop(self, e, f):
        memo = [[None for i in range(f+1)]
                           for j in range(e+1)]
        for i in range(e+1):
            for j in range(2):
                memo[i][j] = j
        for j in range(f+1):
            memo[1][j] = j
        # for row in memo:
        #     print(row)
        for i in range(2, e+1):
            for j in range(2, f+1):
                memo[i][j] = float('inf')
                for k in range(1, j+1):
                    broken = memo[i-1][k-1]
                    # print(i-1, k-1, broken)
                    not_broken = memo[i][j-k]
                    # print(i, j-k, not_broken)
                    res = 1 + max(broken, not_broken)
                    memo[i][j] = min(res, memo[i][j])
        return memo[-1][-1]
        
        
    # def solve(self, e, f):
    #     # print(e, f)
    #     if f<=1:
    #         return f
    #     if e==1:
    #         return f
    #     if self.memo[e][f] != None:
    #         return self.memo[e][f] 
    #     ans = float('inf')
    #     for k in range(1, f+1):
    #         print(e-1, k-1)
    #         broken = self.solve(e-1, k-1)
    #         # we won't check again @ k therefore f-k
    #         print(e, f-k)
    #         not_broken = self.solve(e, f-k)
    #         ans = min(1 + max(broken, not_broken), ans)
    #     self.memo[e][f] = ans
    #     return ans

sol = Solution()
print(sol.eggDrop(4, 10))
# sol.eggDrop(2,2)