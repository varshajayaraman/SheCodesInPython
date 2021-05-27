class SparseVector:
    def __init__(self, nums: List[int]):
        self.rec = set()
        self._vec = nums
        for i in range(len(nums)):
            if nums[i] != 0:
                self.rec.add(i)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        new_rec = set()

        int_set = self.rec and vec.rec
        res = 0
        for x in int_set:
            res += self._vec[x] * vec._vec[x]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)