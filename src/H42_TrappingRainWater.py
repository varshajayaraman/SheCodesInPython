class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        while l + 1 < len(height) and height[l] <= height[l + 1]:
            l += 1
        while r - 1 > 0 and height[r] <= height[r - 1]:
            r -= 1

        ans = 0
        leftMax, rightMax = 0, 0
        while l < r:
            if height[l] < height[r]:
                if height[l] < leftMax:
                    ans += leftMax - height[l]

                else:
                    leftMax = height[l]
                l += 1
            else:
                if height[r] < rightMax:
                    ans += rightMax - height[r]

                else:
                    rightMax = height[r]
                r -= 1
        return ans