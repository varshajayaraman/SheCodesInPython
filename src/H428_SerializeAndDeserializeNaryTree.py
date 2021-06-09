"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        global res
        res = []

        def rec(node):
            global res
            if not node:
                return

            res.append(str(node.val))
            for c in node.children:
                rec(c)
            res.append("#")

        rec(root)
        return " ".join(res)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        global index
        index = 0

        data = data.split(" ")
        print(data)

        def rec(data):

            global index
            # print(index)
            if index >= len(data) or data[index] == "":
                return None
            if data[index] == "#":
                index += 1
                return

            t = Node(int(data[index]))
            index += 1
            t.children = []
            while index < len(data) and data[index] != "#":
                t.children.append(rec(data))
            index += 1
            return t

        return rec(data)
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))