from typing import Optional

from utils import TreeNode, create_tree


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            if node is None:
                return 0

            left_len = dfs(node.left)
            right_len = dfs(node.right)
            nonlocal res
            res = max(res, left_len + right_len)
            return max(left_len, right_len) + 1

        dfs(root)
        return res


if __name__ == '__main__':
    print(Solution().diameterOfBinaryTree(create_tree('[1,2,3,4,5,null,null]')))
