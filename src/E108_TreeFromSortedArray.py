class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def SortedArrayToBST(self, nums, low, high):
        if low<=high:
            n=len(nums)
            mid = int(low + (high-low)/2)
            print(mid)
            root = TreeNode(nums[mid])
            root.left = self.SortedArrayToBST(nums, low, mid-1)
            root.right = self.SortedArrayToBST(nums, mid+1, high)
            return root