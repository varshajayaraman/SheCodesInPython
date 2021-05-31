# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        data = []

        def postorder(root):
            if not root:
                return []
            l = postorder(root.left)
            r = postorder(root.right)
            return l + r + [str(root.val)]

        data = postorder(root)
        data = " ".join(data)
        # print(data)
        return data

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """

        datax = data.split(" ")
        data = []
        for x in datax:
            if x:
                data.append(int(x))

        def reconstruct(minv, maxv):

            if len(data) == 0 or int(data[-1]) < minv or int(data[-1]) > maxv:
                return

            val = data.pop()
            root = TreeNode(int(val))
            root.right = reconstruct(val, maxv)
            root.left = reconstruct(minv, val)
            return root

        return reconstruct(-math.inf, math.inf)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans