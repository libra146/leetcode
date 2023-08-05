from typing import List, Optional

from utils import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = [root]
        while queue:
            sum_ = 0
            q_len = len(queue)
            for a in range(q_len):
                n = queue.pop(0)
                sum_ += n.val
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            res.append(sum_ / q_len)
        return res
