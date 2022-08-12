#User function Template for python3

# class Solution:        
#     def maxPathSum(self, root):

class Solution:
    def maxPathSum(self,root):
        self.ans = float('-inf')
        self.root = root
        # self.showTree(root)
        self.solve(root)
        return self.ans
    
    # def showTree(self, node):
    #     if node == None:
    #         return
    #     print(node.data)
    #     self.showTree(node.left)
    #     print('-------')
    #     self.showTree(node.right)
        
        
    def solve(self, node):
        # Base Condition
        if node == None:
            return 0
        
        # Hypothesis
        lData = self.solve(node.left)
        rData = self.solve(node.right)
        
        #induction
        if node.left != None and node.right != None:
            self.ans = max(node.data + lData + rData, self.ans)
        if node == self.root and (node.left == None or node.right==None):
            self.ans = max(node.data + lData + rData, self.ans)
        if node.left == None and node.right == None:
            print(node.data, max(node.data, node.data+max(lData, rData)), self.ans)
            return max(node.data, node.data+max(lData, rData))
        elif node.left == None and node.right != None:
            print(node.data, node.data+rData)
            return node.data + rData
        elif node.right == None and node.left != None:
            print(node.data, node.data+lData)
            return node.data + lData
        else:
            print(node.data, node.data+max(lData, rData), self.ans)
            return node.data+max(lData, rData)
        
        # #induction
        # if node.left!=None and node.right!=None:
        #     # print(node.data, lVal, rVal, node.data+lVal+rVal)
        #     self.ans = max(self.ans, node.data+lVal+rVal)
        # if node.right == None:
        #     print('*', node.data, node.data+lVal)
        #     return node.data+lVal
        # # print(node.data, node.data+max(lVal, rVal))
        # return node.data+max(lVal, rVal)
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import deque
import sys
sys.setrecursionlimit(10**6)  #Increasing the limit of recursion
# Tree Node
class Node:
   def __init__(self, val):
       self.right = None
       self.data = val
       self.left = None


# Function to Build Tree   
def buildTree(s):
   #Corner Case
   if(len(s)==0 or s[0]=="N"):           
       return None
       
   # Creating list of strings from input 
   # string after spliting by space
   ip=list(map(str,s.split()))
   
   # Create the root of the tree
   root=Node(int(ip[0]))                     
   size=0
   q=deque()
   
   # Push the root to the queue
   q.append(root)                            
   size=size+1 
   
   # Starting from the second element
   i=1                                       
   while(size>0 and i<len(ip)):
       # Get and remove the front of the queue
       currNode=q[0]
       q.popleft()
       size=size-1
       
       # Get the current node's value from the string
       currVal=ip[i]
       
       # If the left child is not null
       if(currVal!="N"):
           
           # Create the left child for the current node
           currNode.left=Node(int(currVal))
           
           # Push it to the queue
           q.append(currNode.left)
           size=size+1
       # For the right child
       i=i+1
       if(i>=len(ip)):
           break
       currVal=ip[i]
       
       # If the right child is not null
       if(currVal!="N"):
           
           # Create the right child for the current node
           currNode.right=Node(int(currVal))
           
           # Push it to the queue
           q.append(currNode.right)
           size=size+1
       i=i+1
   return root

if __name__=="__main__":
    # t=int(input())
    t = 1
    for _ in range(0,t):
        # s=input()
        # print(s, type(s))
        s = "3 4 5 -10 4"
        s = "-9 6 -10"
        s = "1 8 6 -7 -10 -9"
        # s = "9 4 6 N -7 3 -7 N 6"
        s = "5 N 6 -5 5"
        root=buildTree(s)
        ob = Solution()
        print(ob.maxPathSum(root))
# } Driver Code Ends