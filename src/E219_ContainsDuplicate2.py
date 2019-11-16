def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    res = {}
    for i in range(len(nums)):
        if nums[i] not in res.keys():
            res[nums[i]] = i
        else:
            if i - res[nums[i]] <= k:
                return True
            else:
                res[nums[i]] = i
    return False