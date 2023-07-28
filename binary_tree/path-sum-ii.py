from typing import Optional, List

from utils import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        result = []

        def dfs(node, res, s):
            if not node:
                return
            res.append(node.val)
            s -= node.val
            print(res)
            if not node.left and not node.right and s == 0:
                result.append(list(res))
            dfs(node.left, res, s)
            dfs(node.right, res, s)
            res.pop()

        dfs(root, [], targetSum)
        return result
