from typing import Optional

from utils import TreeNode


class Solution:
    def __init__(self):
        self.res = 0

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root:
            return 0
        print(root.val)
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        print(left, right)
        p = abs(left - right)
        self.res += p
        return left + right + root.val
