from typing import Optional

from utils import TreeNode, create_tree


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        depth = 1
        if root is None:
            return res
        queue = [(root, depth)]
        while queue:
            node, depth = queue.pop()
            # 如果是根节点的值，或者是子节点，后退
            if isinstance(node, int) or node is None:
                depth -= 1
                continue
            # 到达最底层，计算层级
            if node.left is None and node.right is None:
                res = max(res, depth)
                continue
            # 如果有后续节点，往后面遍历
            if node.left or node.right:
                depth += 1
                queue.append((node.left, depth))
                queue.append((node.val, depth))
                queue.append((node.right, depth))
        return res


if __name__ == '__main__':
    print(Solution().maxDepth(create_tree('[3,9,20,null,null,15,7]')))
    print(Solution().maxDepth(create_tree('[1,null,2]')))
