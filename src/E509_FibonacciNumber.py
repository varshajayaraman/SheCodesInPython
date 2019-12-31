class Solution:
    def fib(self, N: int) -> int:
        res=[0 for i in range(N+1)]
        if N==0:
            return 0
        if N==1:
            return 1
        res[1]=1
        for i in range(2,N+1):
            res[i]=res[i-1]+res[i-2]
        print(res)
        return res[N]