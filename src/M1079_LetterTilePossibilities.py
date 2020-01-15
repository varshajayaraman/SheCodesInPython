class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = {""}

        def append(char, st, res):
            # global res

            for i in range(len(st) + 1):
                # print(char, st, i)
                # print("To add: ", st[:i]+char+st[i:])
                res.add(st[:i] + char + st[i:])

        def recFn(tiles, ind, res):
            if ind == len(tiles):
                return

            if ind == 0:
                res.add(tiles[ind])
                recFn(tiles, ind + 1, res)
                return
            # print(res)
            lres = [x for x in res]
            for i in lres:
                # print(lres)
                append(tiles[ind], i, res)
                res.add(tiles[ind])
            recFn(tiles, ind + 1, res)

        res.remove("")
        recFn(tiles, 0, res)
        # print(res)
        return len(res)