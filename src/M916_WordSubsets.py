class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        Bmap = {}
        for b in B:
            bmap = {}
            for a in b:
                if bmap.get(a) is None:
                    bmap[a] = 1
                else:
                    bmap[a] += 1
            for k, v in bmap.items():
                if Bmap.get(k) is None:
                    Bmap[k] = 0
                Bmap[k] = max(Bmap[k], bmap[k])

        res = []
        for a in A:

            flag = True
            amap = {}
            for x in a:
                if amap.get(x) is None:
                    amap[x] = 1
                else:
                    amap[x] += 1
            # print(a, amap, Bmap)
            for k, v in Bmap.items():

                if amap.get(k) is None or amap[k] < v:
                    flag = False
                    break
            if flag is True:
                res.append(a)

        return res
