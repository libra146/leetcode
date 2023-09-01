from typing import List, Optional

from utils import TreeNode, create_tree


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


class Solution2:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        max_count = 0
        current_val = None
        current_count = 0

        def traverse(node):
            nonlocal current_count, current_val, max_count
            if not node:
                return
            traverse(node.left)
            if current_val == node.val:
                current_count += 1
            else:
                current_val = node.val
                current_count = 1
            if current_count > max_count:
                res.clear()
                max_count = current_count
                res.append(current_val)
            elif current_count == max_count:
                res.append(current_val)
            traverse(node.right)

        traverse(root)
        return res


if __name__ == '__main__':
    print(Solution2().findMode(create_tree('[1,null,2]')))
