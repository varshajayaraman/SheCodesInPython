class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        if len(nums) < 4:
            return []

        nums.sort()
        global res
        res = []
        hmap = {}

        def getSum(nums):
            # print(nums)
            global res
            p1 = 0
            p2 = len(nums) - 1
            if p1 < p2:
                p3 = p1 + 1
                p4 = p2 - 1
                s = nums[p1] + nums[p2]
                su = -999
                while p3 < p4:
                    su = s + nums[p3] + nums[p4]
                    # print(p3,p4, su,target)
                    if s + nums[p3] + nums[p4] == target:
                        if hmap.get((nums[p1], nums[p3], nums[p4], nums[p2])) is None:
                            res.append([nums[p1], nums[p3], nums[p4], nums[p2]])
                            # print(p3,p4)
                            hmap[(nums[p1], nums[p3], nums[p4], nums[p2])] = 1
                    su = s + nums[p3] + nums[p4]
                    if su <= target:
                        p3 += 1
                        while p3 < p4 and nums[p3] == nums[p3 - 1]:
                            p3 += 1
                    if su >= target:
                        p4 -= 1
                        while p3 < p4 and nums[p4] == nums[p4 + 1]:
                            p4 -= 1
                    # print(p3, p4)

        # print(nums)

        def rec(nums):
            oi = 0
            oj = len(nums) - 1
            j = oj
            i = oi
            while oi < oj - 2:
                j = oj
                i = oi
                while i < j - 2:
                    # print("start: ", i, j)
                    getSum(nums[i:j + 1])
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        # print(i,j)
                        j -= 1

                j = oj
                i = oi
                while i < j - 2:
                    # print("start: ",i, j)
                    getSum(nums[i:j + 1])
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                oi += 1
                oj -= 1

        rec(nums)
        return res
