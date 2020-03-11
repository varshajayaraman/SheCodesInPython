class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        hmap = {}

        for i in range(len(wall)):
            s = 0
            for j in range(len(wall[i]) - 1):
                s += wall[i][j]
                if s in hmap:
                    hmap[s] += 1
                else:
                    hmap[s] = 1

        maxV = 0
        for k, v in hmap.items():
            maxV = max(maxV, v)

        return len(wall) - maxV