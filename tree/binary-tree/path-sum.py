from typing import Optional

from utils import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        res = []
        success = False

        def dfs(node):
            nonlocal success
            if success:
                return
            res.append(node.val)
            if not node.left and not node.right:
                if targetSum == sum(res):
                    success = True
                    return
            if node.left:
                dfs(node.left)
                if res:
                    res.pop()
            if node.right:
                dfs(node.right)
                if res:
                    res.pop()

        dfs(root)
        return success


class Solution2:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and targetSum == root.val:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
