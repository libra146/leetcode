from typing import Optional

from utils import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.dfs(root) != -1

    def dfs(self, node):
        if not node:
            return 0
        left_depth = self.dfs(node.left)
        if left_depth == -1:
            return -1
        right_depth = self.dfs(node.right)
        if right_depth == -1:
            return -1
        return max(left_depth, right_depth) + 1 if abs(left_depth - right_depth) < 2 else -1


class Solution2:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        res = True

        def dfs(node):
            nonlocal res
            if node is None:
                return 0
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            if abs(left_depth - right_depth) > 1:
                res = False
            return max(left_depth, right_depth) + 1

        l = dfs(root.left)
        r = dfs(root.right)
        return all([res, abs(l - r) <= 1])
