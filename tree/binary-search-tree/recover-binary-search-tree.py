from typing import Optional

from utils import TreeNode


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        one = None
        two = None
        self.traverse(root, res)
        for a in range(len(res) - 1):
            if res[a].val > res[a + 1].val:
                two = res[a + 1]
                if one is None:
                    one = res[a]
        if one and two:
            one.val, two.val = two.val, one.val

    def traverse(self, node: Optional[TreeNode], res):
        if not node:
            return
        # 中序遍历
        self.traverse(node.left, res)
        res.append(node)
        self.traverse(node.right, res)
