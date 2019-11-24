import heapq
class Solution:
    def findKthLargest(self, nums, k) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        if len(nums)>k:
            for i in range(k,len(nums)):
                if nums[i]>heap[0]:
                    heapq.heapreplace(heap, nums[i])
        if len(heap)==0:
            return 0
        else:
            return heap[0]