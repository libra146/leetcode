from typing import Optional

from utils import TreeNode, create_tree


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        if not root.left and not root.right:
            return str(root.val)
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        if left != '' and right == '':
            return str(root.val) + f'({left})'
        return str(root.val) + f'({left})({right})'


class Solution2:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        if not root.left and not root.right:
            return str(root.val)
        if root.right is None:
            return str(root.val) + f'({self.tree2str(root.left)})'
        return str(root.val) + f'({self.tree2str(root.left)})({self.tree2str(root.right)})'


if __name__ == '__main__':
    print(Solution2().tree2str(create_tree('[1,2,3,null,4]')))
