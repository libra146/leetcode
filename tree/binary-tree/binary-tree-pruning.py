from typing import Optional

from utils import TreeNode, create_tree


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.traverse(root)

    def traverse(self, root):
        if not root:
            return None
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        if root.val == 0 and left is None and right is None:
            return None
        root.left = left
        root.right = right
        return root


if __name__ == '__main__':
    Solution().pruneTree(create_tree('[0,null,0,0,0]'))
