# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        def maxe(nums, low, high):
            if low == high:
                return low
            if low > high:
                return None
            res = low
            for i in range(low + 1, high + 1):
                if nums[i] > nums[res]:
                    res = i
            return res

        def f(nums, low, high):
            mid = maxe(nums, low, high)
            print(low, mid, high)
            if mid is None:
                return None
            root = TreeNode(nums[mid])
            print("Right")
            root.right = f(nums, mid + 1, high)
            print("Left")
            root.left = f(nums, low, mid - 1)
            return root

        return f(nums, 0, len(nums) - 1)