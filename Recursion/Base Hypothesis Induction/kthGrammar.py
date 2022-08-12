"""
Created on Sat Apr 23 21:24:54 2022

@author: Kuldeep
"""
class Solution:
    def kthGrammar(self, n, k):
        if n==1:
            return 0
        # 1 - 1
        # 2 - 2
        # 3 - 4
        # 4 - 8
        mid = int((2**(n-1))/2)
        if k <= mid:
            # print('-', n, k)
            return self.kthGrammar(n-1, k)
        else:
            # print('*', n, k, k, k%x)
            return int(not self.kthGrammar(n-1, k-mid))

if __name__=='__main__':
    sol = Solution()
    print(sol.kthGrammar(3, 3))
