"""
Created on Sat Apr 23 17:30:16 2022

@author: Kuldeep
"""

class Solution():
    def fun(self, arr):    
        return self.solve(arr)
    
    def solve(self, arr):
        # Base Condition
        if len(arr)==1:
            return arr
        
        # Hypothesis
        n = len(arr)
        sorted_arr = self.solve(arr[:n-1])
        element = arr[n-1]
        
        # print(sorted_arr, element)
        #Induction
        index = n-1
        for i in range(n-1):
            if arr[i]>element:
                # print('\t', arr[i], i)
                index = i
                break
        sorted_arr.insert(index, element)
        # print(n-1)
        # print(sorted_arr)
        # print('---------')
        return sorted_arr
            
        
        
        
if __name__=='__main__':
    sol = Solution()
    arr = [1, 4, 3, 5]
    print(sol.fun(arr))
