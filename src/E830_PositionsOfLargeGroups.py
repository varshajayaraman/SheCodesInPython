class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        
        heap = []
        heapq.heapify(heap)
        count = 1
        start=0
        for i in range(1,len(s)):
            # print(i, count, s[i], s[i-1])
            if s[i]==s[i-1]:
                count +=1
            else:
                if count>=3:
                    end = i-1
                    heapq.heappush(heap, [start, end])
                start=i
                end=0
                count = 1
        # print(heap)
        if count>=3:
            heapq.heappush(heap, [start, len(s)-1])
        res = []
        while len(heap)>0:
            res.append(heapq.heappop(heap))
        return res