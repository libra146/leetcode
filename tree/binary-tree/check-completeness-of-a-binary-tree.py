from typing import Optional

from utils import TreeNode


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root and root.left is None and root.right is not None:
            return False
        if root.left is None and root.right is None:
            return True
        res = [root]
        result = []
        while res:
            node = res.pop(0)
            if node is None or (node.left is None and node.right is None):
                result.append(node)
            if node:
                res.append(node.left)
                res.append(node.right)
        while True:
            if result[-1] is None:
                result.pop()
            else:
                break
        return all(result)


class Solution2:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        res = [root]
        while res:
            node = res.pop(0)
            if node is None:
                break
            else:
                res.append(node.left)
                res.append(node.right)
        while res and res[0] is None:
            res.pop(0)
        return not res
