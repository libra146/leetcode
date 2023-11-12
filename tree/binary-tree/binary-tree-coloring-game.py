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
        self.res = False

    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        self.traverse(root, n, x)
        return self.res

    def traverse(self, root, n, x):
        if not root:
            return 0
        left = self.traverse(root.left, n, x)
        right = self.traverse(root.right, n, x)
        if x == root.val and (left > n / 2 or right > n / 2 or n - left - right - 1 > n / 2):
            self.res = True
        return left + right + 1
# leetcode submit region end(Prohibit modification and deletion)
