class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_angle = 360 // 60
        hour_angle = 360 // 12

        min_move = minutes * min_angle
        hour_move = ((hour % 12) + (minutes / 60)) * hour_angle

        diff = abs(hour_move - min_move)
        return min(diff, 360 - diff)