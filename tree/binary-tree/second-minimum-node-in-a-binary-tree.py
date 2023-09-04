from typing import Optional

from utils import TreeNode


class Solution:
    def __init__(self):
        self.res = {}

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        if root.val not in self.res:
            self.res[root.val] = 0
        self.findSecondMinimumValue(root.left)
        self.findSecondMinimumValue(root.right)
        v = list(self.res.keys())
        v.sort()
        return v[1] if len(v) > 1 else None
