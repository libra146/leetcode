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

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.traverse(root, '')
        return self.res

    def traverse(self, root, path):
        if not root:
            return
        if not root.left and not root.right:
            self.res += int(f'{path}{root.val}', 2)
        self.traverse(root.left, f'{path}{root.val}')
        self.traverse(root.right, f'{path}{root.val}')

# leetcode submit region end(Prohibit modification and deletion)
