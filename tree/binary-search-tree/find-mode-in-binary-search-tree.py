from typing import List, Optional

from utils import TreeNode


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hash_map = {}

        def traverse(node):
            if not node:
                return
            if hash_map.get(node.val) is None:
                hash_map[node.val] = 0
            else:
                hash_map[node.val] += 1
            traverse(node.left)

            traverse(node.right)

        traverse(root)
        value = max(hash_map.values())
        return [a for a in hash_map.keys() if hash_map[a] == value]
