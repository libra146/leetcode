from typing import Optional

from utils import TreeNode


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        return self.is_same_tree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,
                                                                                                        subRoot)

    def is_same_tree(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        return node1 and node2 and self.is_same_tree(node1.left, node2.left) and self.is_same_tree(node1.right,
                                                                                                   node2.right) and node1.val == node2.val
