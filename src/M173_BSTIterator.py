# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.container = []
        self.curr = -1
        if root:
            self.inorder(root)
        self.capacity = len(self.container)

    def inorder(self, root):
        if root.left:
            self.inorder(root.left)
        self.container.append(root.val)
        if root.right:
            self.inorder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.curr += 1
        return self.container[self.curr]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return (self.curr + 1) != self.capacity

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()