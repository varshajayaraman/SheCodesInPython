class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return None

        def pushele(x, y):
            print(-abs(-x - (-y)))
            return -abs(-x - (-y))

        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            if stones[0] == stones[1]:
                heapq.heappop(stones)
                heapq.heappop(stones)
            else:
                x = heapq.heappop(stones)
                print(x, stones[0])
                print(stones)
                print(pushele(x, stones[0]))
                heapq.heapreplace(stones, pushele(x, stones[0]))
                print(stones)
        if len(stones) == 0:
            return 0
        else:
            stones = -stones[0]
        return stones

