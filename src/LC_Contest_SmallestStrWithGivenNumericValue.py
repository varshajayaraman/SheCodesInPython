class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        t=n
        n=k
        k=t
        res = []
        while n>0:
            safe = n-(k-1)
            if safe>=26:
                # print(n,k,26)
                res.append(chr(96+26))
                n-=26
                k-=1
            else:
                # print(n,k,safe)
                res.append(chr(96+safe))
                n-=safe
                k-=1
        res.reverse()
        return "".join(res)
        