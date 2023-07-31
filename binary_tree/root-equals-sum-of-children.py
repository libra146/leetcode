from typing import Optional

from utils import TreeNode


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return root.left.val + root.right.val == root.val
