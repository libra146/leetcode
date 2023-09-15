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
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.traverse(root)[0]

    def traverse(self, root):
        if not root:
            return None, 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        if left[1] == right[1]:
            return root, right[1] + 1
        else:
            if left[1] > right[1]:
                return left[0], left[1] + 1
            else:
                return right[0], right[1] + 1
# leetcode submit region end(Prohibit modification and deletion)
