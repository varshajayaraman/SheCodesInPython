class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        if len(groupSizes) == 0:
            return []
        res = []
        hmap = {}
        for i in range(len(groupSizes)):
            if hmap.get(groupSizes[i]) is None:
                hmap[groupSizes[i]] = [i]
            else:
                hmap[groupSizes[i]].append(i)

        print(hmap)
        for k, v in hmap.items():
            if len(v) == k:
                res.append(v)
            else:
                i = 0
                while i < len(v):
                    res.append(v[i:i + k])
                    i += k

        return res