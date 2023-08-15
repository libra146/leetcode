from typing import Optional

from utils import TreeNode


class Solution:
    num = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root

    def traverse(self, node: Optional[TreeNode]):
        if not node:
            return
        self.traverse(node.right)
        self.num += node.val
        node.val = self.num
        self.traverse(node.left)
