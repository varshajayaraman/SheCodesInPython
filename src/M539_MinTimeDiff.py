class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        for i in range(len(timePoints)):
            timePoints[i] = int(timePoints[i].split(":")[0]) * 60 + int(timePoints[i].split(":")[1])
        timePoints.sort()

        minRes = math.inf

        for i in range(1, len(timePoints)):
            minRes = min(minRes, timePoints[i] - timePoints[i - 1])

        l = len(timePoints) - 1
        minRes = min(minRes, 24 * 60 - timePoints[l] + timePoints[0])
        return minRes