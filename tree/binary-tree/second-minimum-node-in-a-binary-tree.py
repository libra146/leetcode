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


class Solution2:

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.left is None:
            return -1
        left = root.left.val
        right = root.right.val
        if root.val == root.right.val:
            right = self.findSecondMinimumValue(root.right)
        if root.val == root.left.val:
            left = self.findSecondMinimumValue(root.left)
        if right == -1:
            return left
        if left == -1:
            return right
        return min(left, right)
