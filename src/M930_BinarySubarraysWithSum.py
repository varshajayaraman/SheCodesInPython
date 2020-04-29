class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:

        s = 0
        h = {}
        res = 0
        count = 0
        for j in range(len(A)):
            s += A[j]

            if s == S:
                res += 1

            if h.get(s - S) is not None:
                res += h[s - S]
            if h.get(s) is None:
                h[s] = 1
            else:
                h[s] += 1

        return res