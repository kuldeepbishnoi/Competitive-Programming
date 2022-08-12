"""
Created on Sun Apr 10 17:19:37 2022

@author: Kuldeep
"""

class Solution():
    def _01_knapsack(self, weights, values, w):
        '''
        Problem:
            
            Time Complexity : O()
            Space Analysis  : O()
        
        Logic: 
            
        Link: 
        '''
        # weights, values = (list(t) for t in zip(*sorted(zip(weights, values))))
        
        self.w = w
        self.weights = weights
        self.values = values
        self.size = len(weights)
        
        return self.solve(0, 0)
    
    def solve(self, index, current_weight):
    
        if current_weight == 0 or index == self.size:
            return 0
        
        included = float('-inf')
        
        if current_weight - self.weights[index] <= self.w:
            included = self.values[index] + self.solve(index+1, current_weight + self.weights[index])
        not_included = self.solve(index + 1, current_weight)
        
        return max(included, not_included)
            
        
        
if __name__=='__main__':
    weights = []
    values = []
    sol = Solution()
    print(sol._01_knapsack())
