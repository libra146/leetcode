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
        self.cnt = 0

    def findTargetNode(self, root: Optional[TreeNode], cnt: int) -> int:
        self.cnt = cnt
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root or self.res:
            return
        self.traverse(root.right)
        self.cnt -= 1
        if self.cnt == 0:
            self.res = root.val
        self.traverse(root.left)
# leetcode submit region end(Prohibit modification and deletion)
