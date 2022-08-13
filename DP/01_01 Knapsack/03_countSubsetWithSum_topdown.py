class Solution:
    def perfectSum (self, arr, N, S):
        memo = [[0 for i in range(S+1)]
                for j in range(N+1)]
        
        for n in range(N+1):
            for s in range(S+1):
                if n==0:
                    if s==0:
                        memo[n][s] = 1
                    else:
                        memo[n][s] = 0
        
        for n in range(1, N+1):
            for s in range(0, S+1):
                if s-arr[n-1]>=0:
                    memo[n][s] = memo[n-1][s-arr[n-1]] +\
                                memo[n-1][s]
                else:
                    memo[n][s] = memo[n-1][s]
        
        return memo[-1][-1] % (10**9 + 7)


if __name__=='__main__':
    sol = Solution()
    arr = [9,7,0,3,9,8,6,5,7,6]
    print(sol.perfectSum(arr, len(arr), 31))