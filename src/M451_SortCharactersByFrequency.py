class Solution:
    def frequencySort(self, s: str) -> str:
        def getString(char, count):
            s = ""
            while count > 0:
                s += char
                count -= 1
            return s

        cd = {}
        for i in s:
            if i in cd.keys():
                cd[i] += 1
            else:
                cd[i] = 1
        heap = []
        for c, v in cd.items():
            heap.append((v, c))
        heapq.heapify(heap)
        res = ""
        while len(heap) > 0:
            v, c = heapq.heappop(heap)
            res = getString(c, v) + res

        return res