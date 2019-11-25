class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nd = {}
        for i in nums:
            if i in nd.keys():
                nd[i] += 1
            else:
                nd[i] = 0

        heap = []
        i = 1
        for e, v in nd.items():
            if i <= k:
                heap.append((v, str(e)))
                if i == k:
                    heapq.heapify(heap)
                i += 1
                continue
            else:
                if v >= heap[0][0]:
                    heapq.heapreplace(heap, (v, str(e)))

        res = []
        i = len(heap) - 1
        while i >= 0:
            res.append(int(heap[i][1]))
            i -= 1
        return res
