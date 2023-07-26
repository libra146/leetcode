from typing import Optional

from utils import TreeNode


class Solution:
    # 如果根节点为null，返回true。如果根节点值和左右子树值相同并且左右子树都是单值树返回true
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        def traverse(node):
            if not node:
                return True
            if node.left is not None and node.val != node.left.val:
                return False
            if node.right is not None and node.val != node.right.val:
                return False
            return traverse(node.left) and traverse(node.right)

        return traverse(root)
