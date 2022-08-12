"""
Created on Wed Apr 20 18:17:35 2022

@author: Kuldeep
"""

import functools
class Solution():
    @functools.lru_cache(maxsize=None)
    def countDivisor(self, n):
        ans = 0
        for i in range(1, n):
            if n%i==0:
                ans += 1
        return ans
        
    def fun(self, n, arr):
        ans = 0
        divisor = []
        
        for i in arr:
            divisor.append(self.countDivisor(i))
            
        for i in range(0, n):
            for j in range(i, n):
                divisor_count = 0
                # print(i, j)
                for k in range(i, j+1):
                    # print('\t', k)
                    divisor_count += divisor[k]
                if divisor_count % 2 != 0:
                    ans += 1
                # print(divisor_count)
                # print('*'*10)
        return ans
            
if __name__=='__main__':
    sol = Solution()
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    # arr = [12, 36, 2, 21]
    print(sol.fun(len(arr), arr))
