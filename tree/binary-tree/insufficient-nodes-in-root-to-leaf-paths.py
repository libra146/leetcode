from typing import Optional

from utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        if not root:
            return
        if not root.left and not root.right:
            if root.val < limit:
                return
            return root
        left = self.sufficientSubset(root.left, limit - root.val)
        right = self.sufficientSubset(root.right, limit - root.val)
        if not left and not right:
            return None
        root.left = left
        root.right = right
        return root
# leetcode submit region end(Prohibit modification and deletion)
