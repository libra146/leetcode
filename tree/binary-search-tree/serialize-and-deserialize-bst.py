from typing import Optional

from utils import TreeNode, create_tree


class Codec:
    def __init__(self):
        self.res = []
        self.nodes = []

    def serialize(self, root: Optional[TreeNode]) -> str:

        """Encodes a tree to a single string.
        """
        if not root:
            return ''
        self._serialize(root)
        return ','.join(map(str, self.res))

    def _serialize(self, root):
        if not root:
            return
        self.res.append(root.val)
        self._serialize(root.left)
        self._serialize(root.right)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        self.nodes = list(map(int, data.split(',')))
        return self._deserialize(float('-inf'), float('inf'))

    def _deserialize(self, min, max):
        if not self.nodes:
            return
        value = self.nodes[0]
        if value > max or value < min:
            return None
        else:
            root_val = self.nodes.pop(0)
        root = TreeNode(root_val)
        root.left = self._deserialize(min, root_val)
        root.right = self._deserialize(root_val, max)
        return root


if __name__ == '__main__':
    for a in range(10000):
        ser = Codec()
        deser = Codec()
        tree = ser.serialize(create_tree('[2,1,3]'))
        ans = deser.deserialize(tree)
        # print(ans)
