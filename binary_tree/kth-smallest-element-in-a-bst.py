from typing import Optional

from utils import TreeNode


class Solution:
    result = None
    index = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return
        self.kthSmallest(root.left, k)
        self.index += 1
        if self.index == k:
            self.result = root.val
            return self.result
        self.kthSmallest(root.right, k)
        return self.result
