
'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        return self.solve(root)
    
    def solve(self, node):
        if node==None:
            return 0
        
        return 1+max(self.solve(node.left), self.solve(node.right))