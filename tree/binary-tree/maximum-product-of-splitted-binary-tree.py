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
        self.sum = 0

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.sum_node(root)
        self.traverse(root)
        return self.res % (10 ** 9 + 7)

    def sum_node(self, root):
        if not root:
            return
        self.sum_node(root.left)
        self.sum_node(root.right)
        self.sum += root.val

    def traverse(self, root):
        if not root:
            return
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        left = left if left else 0
        right = right if right else 0
        self.res = max(self.res, right * (self.sum - right), left * (self.sum - left))
        return root.val + left + right

# leetcode submit region end(Prohibit modification and deletion)
