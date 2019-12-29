class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res=x^y
        c=0
        while res>0:
            if res&1==1:
                c+=1
            res>>=1
        return c