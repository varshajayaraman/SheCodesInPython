class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def isValidIp(s):
            if len(s) == 0:
                return False
            if s[0] == "0" and len(s) > 1:
                return False
            s = int(s)
            return 0 <= s <= 255

        global res
        res = set([])

        def rec(curr, start):
            global res
            if len(curr) == 4:
                if start == len(s):
                    res.add(".".join(curr))
                return
            # if start>=len(s):
            #     return
            for i in range(3):
                # print(start, i)
                if isValidIp(s[start:start + i + 1]):
                    # print(len(s[start:start+i+1]))
                    rec(curr + [s[start:start + i + 1]], start + i + 1)

        if len(s) < 4:
            return []
        rec([], 0)
        return list(res)