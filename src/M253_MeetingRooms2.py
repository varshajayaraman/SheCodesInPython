class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        if len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 1
        heap = [intervals[0][1]]
        heapq.heapify(heap)

        for i in range(1, len(intervals)):
            if intervals[i][0] >= heap[0]:
                heapq.heapreplace(heap, intervals[i][1])
            else:
                heapq.heappush(heap, intervals[i][1])

        return len(heap)