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

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.traverse(root, root)
        return self.res

    def traverse(self, root, pre):
        if not root:
            return 0
        left = self.traverse(root.left, root)
        right = self.traverse(root.right, root)
        self.res = max(left + right, self.res)
        if root.val != pre.val:
            return 0
        return max(left, right) + 1

# leetcode submit region end(Prohibit modification and deletion)
