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
    def checkSymmetricTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.traverse(root.left, root.right)

    def traverse(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 and root2:
            if root1.val != root2.val:
                return False
            left = self.traverse(root1.left, root2.right)
            right = self.traverse(root1.right, root2.left)
            return left and right
        else:
            return False
# leetcode submit region end(Prohibit modification and deletion)
