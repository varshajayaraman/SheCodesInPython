class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if m == 0:
            for x in range(len(nums2)):
                nums1[x] = nums2[x]
            return nums1
        if n == 0:
            return nums1

        p = len(nums1) - 1
        p1 = m - 1
        p2 = len(nums2) - 1
        while p1 >= 0 and p2 >= 0 and p > p1:
            if nums2[p2] > nums1[p1]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        if p1 == p or p2 < 0:
            return nums1
        if p1 < 0:
            while p2 >= 0:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1
        return nums1