from typing import Optional

from utils import TreeNode


class Solution:

    def __init__(self):
        self.res = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        # 因为要取最大值，所以负值要过滤掉
        left = left if left > 0 else 0
        right = right if right > 0 else 0
        self.res = max(self.res, root.val + left + right)
        # 取的是当前节点和最大的子节点，不是路径
        return root.val + max(left, right)
