"""
Tags:
    -
    
Time: O()
Space: O()
    
Apprach:
    Option1: Similar to 
        -
        
Problem:
    
    
"""

if __name__=='__main__':
    adj = []
    flag = True
    with open(r'C:\Users\kulde\Desktop\fileInput.txt') as f:
        for line in f:
            if flag:
                u, _ = map(int, line.strip().split())
                adj = [[] for _ in range(u+1)]
                flag = False
                
            u, v = map(int, line.strip().split())    
            adj[u].append(v)
            
    with open('fileOutput.txt', 'w') as f:  
        for ls in adj[1:]:
            f.write(" ".join(str(i) for i in ls) + '\n')
    