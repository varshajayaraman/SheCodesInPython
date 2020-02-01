class Solution:
    def maxArea(self, height: List[int]) -> int:

        maxArea = 0
        i = 0
        j = len(height) - 1
        while i < j:
            # print(maxArea, i, j, height[i], height[j])
            # print(j-i, min(height[i], height[j]), min(height[i], height[j])*(j-i))
            maxArea = max(maxArea, min(height[i], height[j]) * (j - i))
            if height[j] <= height[i]:
                j -= 1
            else:
                i += 1
        return maxArea