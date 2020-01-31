class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1 for i in nums]
        backward = [1 for i in nums]
        res = [1 for i in nums]
        l = len(nums)
        forward[0] = nums[0]
        backward[l - 1] = nums[l - 1]
        if len(nums) == 0:
            return 0
        for i in range(l - 2, -1, -1):
            backward[i] = backward[i + 1] * nums[i]
        for i in range(1, l):
            forward[i] = forward[i - 1] * nums[i]

        # print(backward, forward)
        for i in range(l):
            # print(i)
            if i == 0:
                # print("1", i)
                if i + 1 < l:
                    res[i] = backward[i + 1]
                else:
                    res[i] = 1
            elif i == l - 1:
                # print("2", i)
                if i - 1 >= 0:
                    res[i] = forward[i - 1]
                else:
                    res[i] = 0
            else:
                # print("3", i)
                res[i] = forward[i - 1] * backward[i + 1]

        return res
