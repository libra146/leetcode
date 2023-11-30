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

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root:
            return 0, 0
        left_val, left_num = self.traverse(root.left)
        right_val, right_num = self.traverse(root.right)
        t = (left_val + right_val + root.val) // (left_num + right_num + 1)
        if root.val == t:
            self.res += 1
        return left_val + root.val + right_val, left_num + 1 + right_num

    # leetcode submit region end(Prohibit modification and deletion)
