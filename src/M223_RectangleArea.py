class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:

        area_1 = (C - A) * (D - B)
        area_2 = (G - E) * (H - F)

        left_b = max(A, E)
        right_b = min(C, G)
        top_b = min(D, H)
        bottom_b = max(B, F)

        if right_b - left_b <= 0 or top_b - bottom_b <= 0:
            return area_1 + area_2
        else:
            return area_1 + area_2 - ((right_b - left_b) * (top_b - bottom_b))