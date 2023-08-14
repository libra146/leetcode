import collections

from utils import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []
        if root is None:
            return ''
        self.traverse(root, result)
        return ''.join(result)

    def traverse(self, node: TreeNode, result):
        if node is None:
            result.append('#')
            result.append(',')
            return
        result.append(str(node.val))
        result.append(',')
        self.traverse(node.left, result)
        self.traverse(node.right, result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        queue = collections.deque(data.split(','))
        return self.build(queue)

    def build(self, data):
        if not data:
            return None
        root_value = data.popleft()
        if root_value == '#':
            return None
        root = TreeNode(root_value)
        root.left = self.build(data)
        root.right = self.build(data)
        return root
