class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap=[(-math.inf,0,0) for i in range(K)]
        heapq.heapify(heap)
        for i in points:
            diff = math.sqrt(pow(i[0],2)+pow(i[1],2))
            if diff<-heap[0][0]:
                tup = (-diff, str(i[0]), str(i[1]))
                heapq.heapreplace(heap, tup)
        res=[]
        for i in range(K):
            res.append([int(heap[i][1]), int(heap[i][2])])
        return res