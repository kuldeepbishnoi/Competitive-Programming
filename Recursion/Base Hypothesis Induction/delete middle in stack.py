"""
Created on Sat Apr 23 18:06:07 2022

@author: Kuldeep
"""


import math
class Solution:
    def deleteMid(self, s, sizeOfStack):
        middle = math.ceil((sizeOfStack+1)/2)
        return self.solve(s, middle)
    
    def solve(self, s, n):
        # Base Condition
        if n==1:
            s.pop()
            return s
        
        #Hypothesis
        element = s.pop()
        s = self.solve(s, n-1)
        
        # print(element, s)
        #induction
        s.append(element)
        return s
    
if __name__=='__main__':
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    print(sol.deleteMid(arr, len(arr)))
