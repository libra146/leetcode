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
        self.res = float('inf')
        self.pre = None

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root:
            return

        self.traverse(root.left)
        if self.pre:
            self.res = min(abs(self.pre.val - root.val), self.res)
        self.pre = root
        self.traverse(root.right)

# leetcode submit region end(Prohibit modification and deletion)
