class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        # heapq.heapify(heap)
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    count +=1
            heap.append((count, i))
        sorter = lambda a:(a[0], a[1])
        heap = sorted(heap, key=sorter)
        # res=[]
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        heap = [a[1] for a in heap]
        return heap[:k]