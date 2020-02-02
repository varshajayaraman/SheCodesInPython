class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        hmap = {}
        heap = []
        heapq.heapify(heap)
        l = len(arr)
        count = 1
        arr.sort()
        for i in range(1, l):
            if arr[i] == arr[i - 1]:
                count += 1
                if i == l - 1:
                    heapq.heappush(heap, (-count, arr[i]))
                    count = 1
            else:
                heapq.heappush(heap, (-count, arr[i - 1]))
                count = 1
                if i == l - 1:
                    heapq.heappush(heap, (-count, arr[i]))
                    count = 1
        heapq.heapify(heap)
        sumV = 0
        count = 0
        # print(heap)
        half = l // 2
        while sumV < half and len(heap) > 0:
            # print(sumV, half)
            p = heapq.heappop(heap)
            # print(p)
            sumV += -p[0]
            count += 1
        return count
