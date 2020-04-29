class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:

        s = 0
        res = 0
        h = {}
        for n in A:
            s += n
            if K != 0:
                s %= K
            if s == 0:
                res += 1
            if h.get(s) is not None:
                res += h[s]
                h[s] += 1
            else:
                h[s] = 1

        return res