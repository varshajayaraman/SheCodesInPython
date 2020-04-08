class Solution:
    def countElements(self, arr: List[int]) -> int:

        if len(arr) == 0 or len(arr) == 1:
            return 0
        count = 0

        hmap = {}
        for x in arr:
            if hmap.get(x) is None:
                hmap[x] = 1
            else:
                hmap[x] += 1

        print(hmap)
        for i in hmap.keys():
            print(i)
            if hmap.get(i + 1) is not None:
                count += hmap.get(i)

        return count