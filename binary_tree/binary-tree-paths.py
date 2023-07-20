from typing import List, Optional

from utils import TreeNode


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        res = []

        def dfs(node, path):
            if not node.left and not node.right:
                res.append(path + '->' + str(node.val))
                return
            path = path + '->' + str(node.val)
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)

        if not root.left and not root.right:
            return [str(root.val)]
        if root.left:
            dfs(root.left, str(root.val))
        if root.right:
            dfs(root.right, str(root.val))
        return res
