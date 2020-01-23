class Solution:
    def jump(self, nums: List[int]) -> int:
        #         res=[math.inf for x in nums]

        #         res[0]=0

        # for i in range(len(res)):
        #     for j in range(i):
        #         if j+nums[j]>=i:
        #             res[i] = min(res[i], res[j]+1)
        # return res[len(nums)-1]

        #         for i in range(len(nums)):
        #             for j in range(1, nums[i]+1):
        #                 if i+j < len(nums):
        #                     res[i+j] = min(res[i+j], res[i]+1)

        #         return res[len(nums)-1]
        steps = 0
        currStep = 0
        maxStep = 0
        i = 0
        while i < len(nums) - 1:
            maxStep = max(maxStep, i + nums[i])
            if i == currStep:
                # print(currStep)
                steps += 1
                currStep = maxStep
            i += 1
        return steps
