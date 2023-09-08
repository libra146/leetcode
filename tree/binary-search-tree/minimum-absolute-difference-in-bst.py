from typing import Optional

from utils import TreeNode


class Solution:
    def __init__(self):
        self.res = float('inf')
        self.pre = None

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        if self.pre is not None:
            self.res = min(self.res, root.val - self.pre.val)
        self.pre = root
        self.traverse(root.right)
