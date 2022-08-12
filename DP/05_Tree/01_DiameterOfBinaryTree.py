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
        self.ans = max(self.ans, 1+lNode+rNode)
        return 1+max(lNode, rNode)

if __name__=='__main__':
    sol = Solution()
    print(sol.fun())
