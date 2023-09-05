from typing import Optional

from utils import TreeNode


class Solution:
    def __init__(self):
        self.res = {}

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        self.traverse(root)
        values = list(self.res.keys())
        for index, a in enumerate(values):
            if k - a in self.res and values.index(a) != index:
                return True
        return False

    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        self.res[root.val] = 0
        self.traverse(root.right)


class Solution2:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        res = {}

        def traverse(root):
            if not root:
                return False
            if k - root.val in res:
                return True
            res[root.val] = 0

            return traverse(root.left) or traverse(root.right)

        return traverse(root)
