"""
Created on Sat Apr 23 12:30:43 2022

@author: Kuldeep
"""

class Solution:
    def diameter(self,root):
        self.ans = 0
        self.solve(root)
        return self.ans
    
    def solve(self, node):
        # Base Condition
        if node == None:
            return 0
        
        # Hypothesis
        lNode = self.solve(node.left)
        rNode = self.solve(node.right)
        
        #induction
        ## m nhi hun ans tum log dekho
        temp = 1+max(lNode, rNode)
        ## m hi hun ans
        self.ans = max(self.ans, 1+lNode+rNode, temp)
        return temp

if __name__=='__main__':
    sol = Solution()
    print(sol.fun())
