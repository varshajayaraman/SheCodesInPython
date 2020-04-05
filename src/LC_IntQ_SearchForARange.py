class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def search(nums, tar, l, h, left):

            if l < h:
                m = (l + h) // 2
                print(l, h, m)
                if nums[m] == tar:
                    if left:
                        if m - 1 >= 0 and nums[m - 1] == tar:
                            return search(nums, tar, l, m - 1, left)
                        else:
                            print("Returning: ", m)
                            return m
                    else:
                        if m + 1 < len(nums) and nums[m + 1] == tar:
                            return search(nums, tar, m + 1, h, left)
                        else:

                            return m
                elif nums[m] < tar:
                    return search(nums, tar, m + 1, h, left)
                else:
                    return search(nums, tar, l, m - 1, left)
            if l == h and nums[l] == tar:
                return l
            return -1

        if len(nums) == 0:
            return [-1, -1]
        left_ind = search(nums, target, 0, len(nums) - 1, True)
        print(left_ind)
        if left_ind == -1:
            return [-1, -1]

        right_ind = search(nums, target, left_ind, len(nums) - 1, False)

        return [left_ind, right_ind]