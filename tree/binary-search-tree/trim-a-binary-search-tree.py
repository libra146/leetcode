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
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        return self.traverse(root, low, high)

    def traverse(self, root: Optional[TreeNode], low, high):
        if not root:
            return
        if root.val > high:
            return self.traverse(root.left, low, high)
        elif root.val < low:
            return self.traverse(root.right, low, high)
        else:
            root.left = self.traverse(root.left, low, high)
            root.right = self.traverse(root.right, low, high)
            return root

# leetcode submit region end(Prohibit modification and deletion)
