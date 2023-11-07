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
        self.res = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        if abs(left - right) > 1:
            self.res = False
        return max(left, right) + 1
# leetcode submit region end(Prohibit modification and deletion)
