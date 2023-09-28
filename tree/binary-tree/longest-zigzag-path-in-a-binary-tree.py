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

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.traverse(root, 0, 0)
        return self.res

    def traverse(self, root, left, right):
        if not root:
            return
        self.res = max(self.res, left, right)
        self.traverse(root.left, 0, left + 1)
        self.traverse(root.right, right + 1, 0)

# leetcode submit region end(Prohibit modification and deletion)
