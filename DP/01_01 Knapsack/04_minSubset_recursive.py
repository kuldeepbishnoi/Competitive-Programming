
# import functools
class Solution:
    def minDifference(self, arr, N):
        self.arr = arr
        return self.solve(N, 0)
    
    # @functools.lru_cache(maxsize=None)
    def solve(self, idx, S):
        if idx==0:
            return abs(sum(self.arr)-(2*S))
        
        return min(self.solve(idx-1, S+arr[idx-1]),
                       self.solve(idx-1, S))
        
if __name__=='__main__':
    sol = Solution()
    arr = [1, 6, 11, 5]
    print(sol.minDifference(arr, len(arr)))