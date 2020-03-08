class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        def dfs(nums, srcInd, hops, last, right):
            global visited
            currInd = last
            # visited.add()
            nextInd = (currInd + nums[currInd]) % len(nums)
            if nums[currInd] > 0 and not right:
                return False
            if nums[currInd] < 0 and right:
                return False
            if nextInd == srcInd:
                if hops == 0:
                    return False
                else:
                    return True
            else:
                if nextInd in visited:
                    return False
                else:
                    visited.add(nextInd)
                    return dfs(nums, srcInd, hops + 1, nextInd, right)

        global visited

        right = False
        for i in range(len(nums)):
            visited = set()
            # visited[i]=True
            if nums[i] > 0:
                right = True
            if dfs(nums, i, 0, i, right):
                return True
        return False