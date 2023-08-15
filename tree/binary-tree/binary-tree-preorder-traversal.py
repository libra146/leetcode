from typing import Optional, List

from utils import TreeNode


class Solution:
    def __init__(self):
        self.res = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traversal(root)
        return self.res

    def traversal(self, node):
        if not node:
            return
        self.res.append(node.val)
        self.traversal(node.left)
        self.traversal(node.right)
