from typing import Optional, List

from utils import TreeNode


class Solution:
    def __init__(self):
        self.res = []

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traversal(root)
        return self.res

    def traversal(self, node):
        if not node:
            return
        self.traversal(node.left)
        self.traversal(node.right)
        self.res.append(node.val)
