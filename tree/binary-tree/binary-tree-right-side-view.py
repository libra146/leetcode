from typing import List, Optional

from utils import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root]
        res = []
        while q:
            size = len(q)
            n = None
            for _ in range(size):
                n = q.pop(0)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            res.append(n.val)
        return res
