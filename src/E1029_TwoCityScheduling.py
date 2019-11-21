class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key=lambda a: (abs(a[0] - a[1])), reverse=True)
        print(costs)
        n = len(costs)
        n = int(n / 2)
        print(n)
        Sum = 0
        ac = 0
        bc = 0
        for i in costs:
            if i[0] < i[1]:
                if ac < n:
                    print("For i: " + str(i) + " adding 0")
                    Sum += i[0]
                    ac += 1
                    print("AC: " + str(ac))
                    print("SUM: " + str(Sum))
                else:
                    print("For i: " + str(i) + " adding 1 due to limit exceed")
                    Sum += i[1]
                    bc += 1
                    print("BC: " + str(bc))
                    print("SUM: " + str(Sum))
            else:
                print(bc, n)
                if bc < n:
                    print("For i: " + str(i) + " adding 1")
                    Sum += i[1]
                    bc += 1
                    print("BC: " + str(bc))
                    print("SUM: " + str(Sum))
                else:
                    print("For i: " + str(i) + " adding 0 due to limit exceed")
                    Sum += i[0]
                    ac += 1
                    print("AC: " + str(ac))
                    print("SUM: " + str(Sum))
        return Sum
