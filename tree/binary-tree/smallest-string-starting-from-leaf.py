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
        self.res = []

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.traverse(root, '')
        return sorted(self.res, key=lambda x: x)[0]

    def traverse(self, root, path):
        if not root:
            return
        if root.left is None and root.right is None:
            self.res.append(chr(root.val + ord('a')) + path)
        self.traverse(root.left, chr(root.val + ord('a')) + path)
        self.traverse(root.right, chr(root.val + ord('a')) + path)

# leetcode submit region end(Prohibit modification and deletion)
