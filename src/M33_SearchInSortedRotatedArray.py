class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bsearch(nums, low, high, t):
            print(low, high)
            if low <= high:
                mid = low + (high - low) // 2

                if nums[mid] == t:
                    return mid

                if nums[low] <= nums[mid] and nums[mid] < t:
                    # right
                    return bsearch(nums, mid + 1, high, t)
                elif nums[low] <= nums[mid] and nums[mid] > t:
                    if nums[low] <= t:
                        # ;eft
                        return bsearch(nums, low, mid - 1, t)
                    else:
                        return bsearch(nums, mid + 1, high, t)
                elif nums[low] > nums[mid] and nums[mid] < t:
                    if nums[low] <= t:
                        # left
                        return bsearch(nums, low, mid - 1, t)
                    else:
                        # right
                        return bsearch(nums, mid + 1, high, t)
                elif nums[low] > nums[mid] and nums[mid] > t:
                    # left
                    return bsearch(nums, low, mid - 1, t)
            return -1

        return bsearch(nums, 0, len(nums) - 1, target)