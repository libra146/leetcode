from typing import Optional

from utils import TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = 0

        def dfs(node, r):
            nonlocal result
            if not node:
                return
            r.append(node.val)
            if not node.left and not node.right:
                result += sum(a * b for a, b in zip([pow(10, aa) for aa in range(len(r) - 1, -1, -1)], r))
            dfs(node.left, r)
            dfs(node.right, r)
            r.pop()

        dfs(root, [])
        return result
