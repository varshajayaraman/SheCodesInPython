class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        h = set()
        c = 0
        if k == 0:
            hmap = {}
            for n in nums:
                if hmap.get(n) is None:
                    hmap[n] = 1
                else:
                    hmap[n] += 1
            for k, v in hmap.items():
                if v > 1:
                    c += 1
            return c
        for n in nums:

            if n in h:
                continue

            if (n + k) in h:
                c += 1
            if (n - k) in h:
                c += 1
            # print(c)
            h.add(n)
        return c