def reverse(S):
    return solve(len(S), S)

def solve(n, S):
    # Base Condition
    if n==0:
        return ""
    
    #Hypothesis
    string = solve(n-1, S)
    return S[n-1] + string 
 
    
#Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
#} Driver Code Ends