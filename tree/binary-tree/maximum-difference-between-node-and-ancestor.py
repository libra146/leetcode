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
    def __init__(self):
        self.res = 0

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.traverse(root, float("-inf"), float("inf"))
        return self.res

    def traverse(self, root, ma, mi):
        if not root:
            return
        ma = max(ma, root.val)
        mi = min(mi, root.val)
        self.res = max(self.res, abs(ma - mi))
        self.traverse(root.left, ma, mi)
        self.traverse(root.right, ma, mi)

        # leetcode submit region end(Prohibit modification and deletion)
