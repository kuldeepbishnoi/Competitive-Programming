class Solution:
    def lcs(self,x,y,s1,s2):
        self.s1 = s1
        self.s2 = s2
        self.memo = [[None for i in range(x+1)]
                            for j in range(y+1)]
        
        ans = self.solve(y, x)
        return ans
    
    def solve(self, idx, till):
        if idx==0 or till<=0:
            return 0
        
        if self.memo[idx][till] != None:
            return self.memo[idx][till]
        
        newTill = self.s1[:till].rfind(self.s2[idx-1])
        if newTill != -1:
            self.memo[idx][till] = max(self.solve(idx-1, till),
                                        1+self.solve(idx-1, newTill))
        else:
            self.memo[idx][till] = self.solve(idx-1, till)            
        return self.memo[idx][till]
        
if __name__=='__main__':
    sol = Solution()
    s1 = 'ABC'
    s2 = 'ABCD'
    print(sol.lcs(len(s1), len(s2), s1, s2))
