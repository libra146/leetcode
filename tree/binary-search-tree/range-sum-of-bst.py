from typing import Optional

from utils import TreeNode


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0

        def traverse(root: Optional[TreeNode], low: int, high: int):
            nonlocal res
            if not root:
                return
            if low <= root.val <= high:
                res += root.val
            if root.val >= low:
                traverse(root.left, low, high)
            if root.val <= high:
                traverse(root.right, low, high)

        traverse(root, low, high)
        return res
