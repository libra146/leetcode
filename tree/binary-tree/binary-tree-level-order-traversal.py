from typing import Optional, List

from utils import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        res = [[root.val]]
        while queue:
            q2 = []
            result = []
            queue_len = len(queue)
            for _ in range(queue_len):
                aa = queue.pop(0)
                result.append(aa.val)
                if aa.left:
                    q2.append(aa.left)
                if aa.right:
                    q2.append(aa.right)
            if result:
                res.append(result)
            queue = q2
        return res
