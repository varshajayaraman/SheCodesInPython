class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = {}
        for x in nums1:
            if h.get(x) is None:
                h[x] = 1
            else:
                h[x] += 1

        res = []
        for x in nums2:
            if h.get(x) is not None and h[x] > 0:
                res.append(x)
                h[x] -= 1

        return res