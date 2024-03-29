class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        l = len(self.nums)
        new_nums = ['a' for i in self.nums]
        for i in range(l):
            r_ind = random.randint(i, l - 1)
            t = new_nums[i]
            new_nums[i] = new_nums[r_ind]
            new_nums[r_ind] = t
        return new_nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()