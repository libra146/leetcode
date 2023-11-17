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
        self.count = 0

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root:
            return
        if not root.left and not root.right:
            self.count ^= (1 << root.val)
            if self.count & (self.count - 1) == 0:
                self.res += 1
            self.count ^= (1 << root.val)
        self.count ^= (1 << root.val)
        self.traverse(root.left)
        self.traverse(root.right)
        self.count ^= (1 << root.val)

# leetcode submit region end(Prohibit modification and deletion)
