from typing import Optional, List

from utils import TreeNode


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        mm = {}

        def find(n):
            if not n:
                return '$'

            left = find(n.left)
            right = find(n.right)
            a = left + ':' + right + ':' + str(n.val)
            vv = mm.get(a, -1)
            if vv == 0:
                res.append(n)
            mm.update({a: vv + 1})
            return a

        find(root)
        return res
