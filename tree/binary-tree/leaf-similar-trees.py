from typing import Optional

from utils import TreeNode


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        res_l = []
        res_r = []

        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]):
            if not node1 and not node2:
                return
            if node1:
                if not node1.left and not node1.right:
                    res_l.append(node1.val)
            if node2:
                if not node2.left and not node2.right:
                    res_r.append(node2.val)
            dfs(node1.left if node1 else None, node2.left if node2 else None)
            dfs(node1.right if node1 else None, node2.right if node2 else None)

        dfs(root1, root2)
        print(res_r, res_l)
        return res_l == res_r
