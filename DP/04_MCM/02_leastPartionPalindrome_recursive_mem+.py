"""
Created on Wed Apr 20 04:22:00 2022

@author: Kuldeep
"""

import functools
class Solution:
    
    def palindromicPartition(self, s):
        self.s = s
        self.memo = [[None for i in range(len(s))]
                             for j in range(len(s))]
        return self.solve(0, len(s)-1)
    
    def solve(self, i, j):
        if i>j:
            print('Alert')
        if i==j:
            return 0
        elif self.isPalindrome(i, j):
            return 0
        if self.memo[i][j] != None:
            return self.memo[i][j]
        ans = float('inf')
        for k in range(i, j):
            if self.memo[i][k] != None:
                left = self.memo[i][k]
            else:
                left = self.solve(i, k)
            
            if self.memo[k+1][j] != None:
                right = self.memo[k+1][j]
            else:
                right = self.solve(k+1, j)
            ans = min(left + right + 1, ans)
        self.memo[i][j] = ans
        return ans
    
    # @functools.lru_cache(maxsize=None)
    # def isPalindrome(self, i, j):
    #     string = self.s[i:j+1]
    #     # print(string)
    #     for i in range(0, int(len(string)/2)):
    #         if string[i] != string[len(string)-i-1]:
    #             return False
    #     return True
    
    def isPalindrome(self, i, j):
        while i<j:
            if self.s[i] != self.s[j]:
                return False
            i+=1
            j-=1
        return True

if __name__=='__main__':
    sol = Solution()
    s = 'aaabba'
    s = 'ababbbabbababa'
    print(sol.palindromicPartition(s))
