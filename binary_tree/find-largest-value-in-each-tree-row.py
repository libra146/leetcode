from typing import List, Optional

from utils import TreeNode


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            r = -float('inf')
            for _ in range(len(queue)):
                n = queue.pop(0)
                r = n.val if n.val > r else r
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            result.append(r)
        return result
