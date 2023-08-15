from typing import Optional

from utils import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, None, None)

    def isValid(self, root: Optional[TreeNode], max_val, min_val):
        if root is None:
            return True
        if max_val is not None and root.val <= max_val.val:
            return False
        if min_val is not None and root.val >= min_val.val:
            return False
        return self.isValid(root.left, max_val, root) and self.isValid(root.right, root, min_val)
