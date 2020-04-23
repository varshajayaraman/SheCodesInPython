class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        if len(s) == 0 or len(s) == 1:
            return s

        def getDirection(shift):
            c = 0
            for i in shift:
                if i[0] == 0:
                    c -= i[1]
                else:
                    c += i[1]
            return c

        c = getDirection(shift)

        print(c)
        if c == 0:
            return s
        hmap = {}
        for i in range(len(s)):
            hmap[i] = ((i + c) % len(s))

        print(hmap)
        res = [0 for i in range(len(s))]
        for k, v in hmap.items():
            print(k, v)
            res[v] = s[k]

        return "".join(res)