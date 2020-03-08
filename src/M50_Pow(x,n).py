class Solution:
    def myPow(self, x: float, n: int) -> float:

        def pow(x, n):
            if n == 1:
                return x

            h = pow(x, n // 2)
            if n % 2 == 0:
                return h * h
            else:
                return h * h * x

        if n == 0:
            return 1
        if n < 0:
            return pow(1 / x, -n)
        else:
            return pow(x, n)

        # if n<0:
        #     x=1/x
        #     n=-n
        # tab = [0 for i in range(n+1)]
        # tab[0]=1
        # if n==0:
        #     return 1
        # tab[1] = x
        # for i in range(2, n+1):
        #     if not n&1:
        #         tab[i] = tab[i//2]*tab[i//2]
        #     else:
        #         tab[i] = tab[i//2]*tab[i//2]*x
        # return tab[n]
