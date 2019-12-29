class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # print((math.log(n)/math.log(3)))
        return n>0 and ((math.log10(n)/math.log10(3))%1)==0