from typing import Optional

from utils import TreeNode, create_tree


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        if ((root1.left is None and root2.left) or (root1.left and root2.left is None)) or (
                root1.left and root2.left and root1.left.val != root2.left.val):
            root1.left, root1.right = root1.right, root1.left
        return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)


class Solution2:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (
                self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))


if __name__ == '__main__':
    print(Solution2().flipEquiv(create_tree('[0,null,1]'),
                                create_tree('[0,null,1]')))
