from typing import Optional

from utils import TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 1
        queue = [root]
        while queue:
            queue_len = len(queue)
            for a in range(queue_len):
                node = queue.pop(0)
                if node.left is None and node.right is None:
                    return depth
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            depth += 1
