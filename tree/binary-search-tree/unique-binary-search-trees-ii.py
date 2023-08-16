from typing import Optional, List

from utils import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        return self.build(1, n)

    def build(self, lo, hi):
        res = []
        if lo > hi:
            res.append(None)
            return res
        for a in range(lo, hi + 1):
            left = self.build(lo, a - 1)
            right = self.build(a + 1, hi)
            for l in left:
                for r in right:
                    root = TreeNode(val=a, left=l, right=r)
                    res.append(root)
        return res
