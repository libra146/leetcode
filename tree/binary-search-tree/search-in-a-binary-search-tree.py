from typing import Optional

from utils import TreeNode


class Solution:
    result = None

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        if val > root.val:
            self.searchBST(root.right, val)
        if val < root.val:
            self.searchBST(root.left, val)
        if val == root.val:
            self.result = root
        return self.result
