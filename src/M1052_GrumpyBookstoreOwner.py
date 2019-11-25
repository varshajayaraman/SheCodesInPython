class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:

        def getsum(a, g, ind, x):
            s = 0
            i = 0
            while i < x:
                if g[ind + i] == 1:
                    s += a[ind + i]
                i += 1
            print(ind, s)
            return s

        gmin, gmax = 0, 0
        maxSave = 0
        for i in range(len(customers) - (X - 1)):
            if i == 0:
                s = getsum(customers, grumpy, i, X)
            else:
                if grumpy[i - 1] == 1:
                    s -= customers[i - 1]
                if grumpy[i + X - 1] == 1:
                    s += customers[i + X - 1]
            if s > maxSave:
                maxSave = s
                gmin = i
                gmax = i + (X - 1)
        print(maxSave, gmin, gmax)

        res = maxSave
        for i in range(len(customers)):
            # if i in range(gmin,gmax+1):
            #     continue
            # else:
            if grumpy[i] == 0:
                print(i)
                res += customers[i]
        return res
