from typing import Optional

from utils import TreeNode, create_tree


class Solution:
    def __init__(self):
        self.res = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        self.traverse(root, targetSum)
        self.pathSum(root.left, targetSum)
        self.pathSum(root.right, targetSum)
        return self.res

    def traverse(self, root, target):
        if not root:
            return
        target -= root.val
        if target == 0:
            self.res += 1
        self.traverse(root.left, target)
        self.traverse(root.right, target)


class Solution2:
    # 前缀和
    # TODO
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pass


if __name__ == '__main__':
    print(Solution().pathSum(create_tree('[1,2,null]'), 2))
