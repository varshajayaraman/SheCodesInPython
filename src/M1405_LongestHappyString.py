class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        def findMax(arr):
            # print("Finding with ", arr)
            m = -1
            for n in range(len(arr)):

                if arr[n] == 0:
                    continue
                if m == -1:
                    m = n
                elif arr[n] > arr[m]:
                    m = n
            # print("Returning ", m)
            return m

        arr = [a, b, c]
        res = []

        g = findMax(arr)

        while g >= 0:
            # print(res, g)
            if len(res) == 0:
                # if arr[g]>1:
                #     res.append(g)
                #     res.append(g)
                #     arr[g]-=2
                # else:
                res.append(g)
                arr[g] -= 1
                g = findMax(arr)
            elif len(res) == 1:
                # if arr[g]>1:
                #     res.append(g)
                #     res.append(g)
                #     arr[g]-=2
                # else:
                res.append(g)
                arr[g] -= 1
                g = findMax(arr)
            else:
                l = len(res)
                if res[l - 1] == g and res[l - 2] == g:
                    g = findMax(arr[:g] + [0] + arr[g + 1:])
                else:
                    # if arr[g]>1:
                    #     res.append(g)
                    #     res.append(g)
                    #     arr[g]-=2
                    # else:
                    res.append(g)
                    arr[g] -= 1
                    g = findMax(arr)
        res1 = []
        for i in res:
            if i == 0: res1.append('a')
            if i == 1: res1.append('b')
            if i == 2: res1.append('c')
        return "".join(res1)