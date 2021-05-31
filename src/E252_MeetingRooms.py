class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True
        if len(intervals) == 1:
            return True
        inte = sorted(intervals)

        for i in range(1, len(inte)):
            if inte[i][0] < inte[i - 1][1]:
                return False
        return True