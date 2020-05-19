class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:

        res = [math.inf, -math.inf, -math.inf, 0, 0]
        tot = 0
        leng = 0
        for i in range(len(count)):
            if count[i] > 0:
                res[0] = min(res[0], i) * 1.0
                res[1] = max(res[1], i) * 1.0
                if count[int(res[4])] < count[i]:
                    res[4] = i * 1.0
                tot += i * count[i]
                leng += count[i]

        res[2] = (tot / leng) * 1.0

        i = 0
        travel = 0
        m1 = 'z'
        m = 0
        while i < len(count):
            while i < len(count) and count[i] == 0:
                i += 1
            if i == len(count):
                return res
            travel += count[i]
            if leng % 2 == 0:
                if travel == leng // 2:
                    m1 = i
                elif travel > leng // 2:
                    if m1 == 'z':
                        res[3] = i * 1.0
                        return res
                    else:
                        res[3] = (m1 + i) / 2.0
                        return res
            elif travel >= leng // 2:
                res[3] = i
                return res
            i += 1