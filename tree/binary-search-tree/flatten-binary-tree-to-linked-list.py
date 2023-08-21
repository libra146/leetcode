from typing import Optional

from utils import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        new_root = TreeNode()
        self.traverse(root, new_root)
        print(new_root)
        root.left = None
        root.right = new_root.right.right

    def traverse(self, root: Optional[TreeNode], new_root: Optional[TreeNode]):
        if not root:
            return new_root
        n = TreeNode(root.val)
        new_root.right = n
        left = self.traverse(root.left, n)
        return self.traverse(root.right, left)
