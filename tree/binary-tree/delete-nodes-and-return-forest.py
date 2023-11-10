from typing import List, Optional

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

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.traverse(root, to_delete, root, '')
        if root.val not in to_delete:
            self.res.append(root)
        return self.res

    def traverse(self, root, to_delete, pre, lor):
        if not root:
            return
        self.traverse(root.left, to_delete, root, 'l')
        self.traverse(root.right, to_delete, root, 'r')
        if root.val in to_delete:
            if root.left:
                self.res.append(root.left)
                root.left = None
            if root.right:
                self.res.append(root.right)
                root.right = None
            if lor == 'l':
                pre.left = None
            else:
                pre.right = None
# leetcode submit region end(Prohibit modification and deletion)
