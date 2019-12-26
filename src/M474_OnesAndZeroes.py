class Solution:

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        def func(strs, m, n, ind, countv):
            global maxCount

            def count(s):
                o, z = 0, 0
                for i in s:
                    if i == '0':
                        z += 1
                    else:
                        o += 1
                return o, z

            def fmax(a, b):
                if a >= b:
                    return a
                else:
                    return b

            # print(ind)
            o, z = count(strs[ind])
            if z <= m and o <= n:
                m -= z
                n -= o
                # print(ind, countv)
                countv += 1

                if (ind + 1) < len(strs):
                    # print(ind, len(strs), "1")
                    func(strs, m, n, ind + 1, countv)
                c = max(maxCount, countv)
                maxCount = c
                if (ind + 2) < len(strs):
                    # print(ind, len(strs), "2")
                    func(strs, m, n, ind + 2, countv)
                c = max(maxCount, countv)
                maxCount = c
            else:
                if (ind + 1) < len(strs):
                    func(strs, m, n, ind + 1, countv)
                c = max(maxCount, countv)
                maxCount = c

        global maxCount
        maxCount = -math.inf
        func(strs, m, n, 0, 0)
        func(strs, m, n, 1, 0)
        m = maxCount
        return m