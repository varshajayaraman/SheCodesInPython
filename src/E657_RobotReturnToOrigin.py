class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0

        for d in moves:
            if d == "U":
                y += 1
            elif d == "D":
                y -= 1
            elif d == "R":
                x += 1
            elif d == "L":
                x -= 1
        return x == 0 and y == 0