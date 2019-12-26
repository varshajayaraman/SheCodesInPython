class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = [0 for l in nums]
        res[len(nums) - 1] = "G"
        lastG = len(nums) - 1
        for x in range(lastG - 1, -1, -1):
            print(nums[x], lastG - x)
            if nums[x] >= lastG - x:
                res[x] = "G"
                lastG = x
            else:
                res[x] = "B"

        print(res)
        if res[0] == "G":
            return True
        else:
            return False