class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) <= k:
            return arr

        ind = bisect_left(arr, x)
        left = ind - 1
        right = ind

        while (right - left - 1) < k:
            if right == len(arr):
                left -= 1
                continue
            if left == -1:
                right += 1
                continue
            if abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        return arr[left + 1:right]