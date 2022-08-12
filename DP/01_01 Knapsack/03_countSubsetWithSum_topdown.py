class Solution:
    def perfectSum (self, arr, N, S):
        memo = [[0 for i in range(S+1)]
                for j in range(N+1)]
        
        # for i in range(0, N+1):
        #     memo[i][0] = 1
        memo[0][0] = 1
        
        for i in range(1, N+1):
            for j in range(0, S+1):
                if arr[i-1]<=j:
                    memo[i][j] = memo[i-1][j-arr[i-1]] +\
                                memo[i-1][j]
                if arr[i-1]>j:
                    memo[i][j] = memo[i-1][j]
        
        return memo[-1][-1]

if __name__=='__main__':
    sol = Solution()
    arr = [9,7,0,3,9,8,6,5,7,6]
    print(sol.perfectSum(arr, len(arr), 31))