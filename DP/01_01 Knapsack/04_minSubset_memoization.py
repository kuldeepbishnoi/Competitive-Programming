
# import functools
class Solution:
    def minDifference(self, arr, N):
        self.arr = arr
        self.memo = [[None for i in range(sum(arr)+1)]
                            for j in range(N+1)]
        self.solve(N, 0)

        return None
    
    # @functools.lru_cache(maxsize=None)
    def solve(self, idx, S):
        if idx==0:
            return abs(sum(self.arr)-(2*S))
        if self.memo[idx][S] != None:
            return self.memo[idx][S]
        
        self.memo[idx][S] = min(self.solve(idx-1, S+arr[idx-1]),
                                self.solve(idx-1, S))
        return self.memo[idx][S]
        
if __name__=='__main__':
    sol = Solution()
    arr = [1, 6, 11, 5]
    print(sol.minDifference(arr, len(arr)))