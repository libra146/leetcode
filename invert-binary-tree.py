from typing import Optional

from utils import TreeNode, create_tree


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invert(root)

    # 针对每个子树，先交换它的左右子树，然后再交换左节点和右节点
    def invert(self, root):
        if root is None:
            return
        left = self.invert(root.left)
        right = self.invert(root.right)
        root.left, root.right = right, left
        return root


class Solution2:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root

    # 针对每个节点，遍历的时候，先交换左右子树，然后再遍历左右子树，进行交换操作
    def traverse(self, root):
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.traverse(root.left)
        self.traverse(root.right)


if __name__ == '__main__':
    Solution().invertTree(create_tree('[4,2,7,1,3,6,9]'))
    Solution2().invertTree(create_tree('[4,2,7,1,3,6,9]'))
