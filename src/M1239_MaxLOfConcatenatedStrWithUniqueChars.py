class Solution:
    def maxLength(self, arr: List[str]) -> int:

        res = []
        maxL = 0
        for x in arr:
            if len(set(x)) == len(x):
                maxL = max(maxL, len(x))
                for m in res:
                    if len(set(m + x)) == len(m + x):
                        res.append(m + x)
                        maxL = max(maxL, len(m + x))
                res.append(x)
        print(res)
        # if len(res)==1:
        #     return len(res[0])
        return maxL