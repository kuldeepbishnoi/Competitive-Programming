class Solution:
    def minDifference(self, arr, N):
        memo = [[False for i in range(sum(arr)+1)]
                        for j in range(N+1)]
        for i in range(0, N+1):
            memo[i][0] = True
        for i in range(1, N+1):
            for j in range(1, sum(arr)+1):
                if arr[i-1]<=j:
                    memo[i][j] = memo[i-1][j-arr[i-1]] or\
                                memo[i-1][j]
                if arr[i-1]>j:
                    memo[i][j] = memo[i-1][j]
        ans = float('inf')
        for i in range(sum(arr)+1):
            if memo[N][i] == True:
                ans = min(ans, abs(sum(arr)-(2*i)))
        return ans
    
if __name__=='__main__':
    sol = Solution()
    arr = [1, 6, 11, 5]
    print(sol.minDifference(arr, len(arr)))