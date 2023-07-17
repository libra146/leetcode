from typing import Optional

from utils import TreeNode, create_tree


class Solution:

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.build(root1, root2)

    def build(self, root1, root2):
        # 有一个节点为 None 就终止遍历，因为后续的节点不用处理了，直接使用
        if root1 is None:
            return root2
        # 同上
        if root2 is None:
            return root1
        # 两边都有节点，将值相加
        root1.val = root2.val + root1.val
        # 继续遍历两个节点的左节点，将结果作为当前节点的左节点
        root1.left = self.build(root1.left, root2.left)
        root1.right = self.build(root1.right, root2.right)
        return root1


if __name__ == '__main__':
    Solution().mergeTrees(create_tree('[1]'), create_tree('[1,2,null]'))
