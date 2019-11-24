class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.oldnums = nums
        self.k = k
        if len(self.oldnums) >= k:
            self.nums = self.oldnums[:k]
            heapq.heapify(self.nums)
            # print(self.nums)
            for i in range(k, len(self.oldnums)):
                self.heapadd(self.oldnums[i], self.nums, k)
        else:
            self.nums = nums
            heapq.heapify(self.nums)

        # print(self.nums)

    def add(self, val: int) -> int:
        self.nums = self.heapadd(val, self.nums, self.k)
        # print(self.nums)
        return self.nums[0]

    def heapadd(self, value: int, nums: List[int], k: int):
        if len(self.nums) >= k:
            if value > self.nums[0]:
                heapq.heapreplace(self.nums, value)

        else:
            heapq.heappush(self.nums, value)
        return self.nums

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)