from typing import Optional

from utils import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        res = []

        def dfs(node: Optional[TreeNode], v):
            if not node:
                return
            if not node.left and not node.right and v == 'l':
                res.append(node.val)
            dfs(node.left, 'l')
            dfs(node.right, 'r')

        dfs(root, '')
        return sum(res)
