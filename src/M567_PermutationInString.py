class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def isSame(h1, h2):
            for k, v in h1.items():
                if h2.get(k) is None or h2[k] != h1[k]:
                    return False
            return True

        s1map = {}
        for i in s1:
            if s1map.get(i) is None:
                s1map[i] = 1
            else:
                s1map[i] += 1

        if len(s1) > len(s2):
            return False
        s2map = {}
        for i in range(len(s1) - 1):
            if s2map.get(s2[i]) is None:
                s2map[s2[i]] = 0
            s2map[s2[i]] += 1

        st = 0
        e = len(s1) - 1

        while e < len(s2):
            if s2map.get(s2[e]) is None:
                s2map[s2[e]] = 0
            s2map[s2[e]] += 1
            if isSame(s2map, s1map):
                return True
            # print(s2map, s1map)
            s2map[s2[st]] -= 1
            if s2map[s2[st]] == 0:
                s2map.pop(s2[st])
            st += 1
            e += 1
        return False
