class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = [math.inf for i in s]
        last=None
        for i in range(len(s)):
            ch = s[i]
            if ch==c:
                last=i
                res[i] = 0
                continue
            elif last==None:
                continue
            else:
                res[i] = abs(i-last)
        # print(res)
        last=None
        for i in range(len(s)-1, -1, -1):
            ch = s[i]
            if ch==c:
                last=i
                res[i] = 0
                continue
            elif last==None:
                continue
            else:
                res[i] = min(abs(i-last), res[i])
        # print(res)
        return res