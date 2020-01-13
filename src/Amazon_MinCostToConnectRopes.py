import heapq
def minCost(nums):
    sumL = 0
    heapq.heapify(nums)
    while len(nums)>1:
        e1 = heapq.heappop(nums)
        e2 = heapq.heappop(nums)
        sumVal = e1+e2
        sumL += sumVal
        heapq.heappush(nums, sumVal)

    print(sumL)