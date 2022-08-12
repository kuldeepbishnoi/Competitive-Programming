"""
Created on Sat Apr 23 17:30:16 2022

@author: Kuldeep
"""

class Solution():
    def fun(self, arr):    
        return self.solve(arr)
    
    def insert(self, arr, element):
        # print('*', arr, element)
        # Base Condition
        if len(arr)==0 or arr[-1]<=element:
            arr.append(element)
            return arr
        
        # Hypothesis
        n = len(arr)
        removed = arr[n-1]
        new_arr = self.insert(arr[:n-1], element)
        
        #induction
        # print(new_arr, removed)
        new_arr.append(removed)
        return new_arr
        
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
        sorted_arr = self.insert(sorted_arr, element)
        return sorted_arr
            
        
        
        
if __name__=='__main__':
    sol = Solution()
    arr = [1, 4, 3, 5, 2]
    print(sol.fun(arr))
