class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        arr = [0 for i in range(26)]
        for s in tasks:
            arr[ord(s) - ord("A")] += 1

        arr = sorted(arr)
        # print(arr)
        maxF = arr.pop()
        min_idle = (maxF - 1) * n

        while len(arr) > 0 and min_idle > 0:
            currMin = min(maxF - 1, arr.pop())
            # print(min_idle, currMin)
            min_idle -= currMin

        if min_idle < 0:
            min_idle = 0

        return min_idle + len(tasks)