class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        res = []
        d = {}
        for itm in items:
            curr = itm[0]
            if curr in d:
                d[curr].append(itm[1])
            else:
                d[curr] = [itm[1]]

        for k, v in d.items():
            d[k].sort(reverse=True)
            print(d[k])
            res.append([k, sum(d[k][:5]) // 5])

        return res