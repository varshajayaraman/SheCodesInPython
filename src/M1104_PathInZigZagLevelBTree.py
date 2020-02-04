class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:

        res = []
        totNodes = 1
        i = 1
        while (totNodes + 2 ** i) < label:
            totNodes += 2 ** i
            i += 1
        level = i

        curr = label
        while curr > 1:
            res.insert(0, curr)
            upper = 2 ** (level + 1) - 1
            lower = 2 ** level
            # print(curr, level, upper, lower)
            curr = math.floor((upper + lower - curr) / 2)
            level -= 1
        res.insert(0, 1)
        return res

