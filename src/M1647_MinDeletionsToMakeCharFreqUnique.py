class Solution:
    def minDeletions(self, s: str) -> int:

        def getMap(word):
            hmap = {}

            for w in word:
                if hmap.get(w):
                    hmap[w] += 1
                else:
                    hmap[w] = 1
            res = {}
            for k, v in hmap.items():
                if res.get(v) is None:
                    res[v] = [k]
                else:
                    res[v].append(k)
            return res

        def getNext(nums, f):
            f -= 1
            while f in nums:
                f -= 1
            return f

        hmap = getMap(s)
        count = 0
        key_list = sorted(hmap.keys())
        freq_set = set(hmap.keys())
        # print(hmap)
        for k in key_list:  # k-num, v-list of chars with frequency k
            v = hmap[k]
            if len(v) > 1:
                for j in range(1, len(v)):
                    freq = getNext(freq_set, k)
                    count += k - freq
                    if freq != 0:
                        freq_set.add(freq)
        return count