from typing import Optional

from utils import TreeNode, create_tree


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traverse(p, q)

    def traverse(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        res1 = self.traverse(node1.left, node2.left)
        res2 = self.traverse(node1.right, node2.right)
        return all([res1, res2])


if __name__ == '__main__':
    print(Solution().isSameTree(create_tree('[1]'), create_tree('[1]')))
