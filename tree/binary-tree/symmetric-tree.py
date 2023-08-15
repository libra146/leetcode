from typing import Optional

from utils import create_tree
from utils.TreeNode import TreeNode


# 定义二叉树


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = root.left
        right = root.right
        # 如果都是 None 说明只有一个节点，返回 true
        if not left and not right:
            return True
        # 将左右节点入栈
        queue = [(left, right)]
        while queue:
            # 遍历栈里面的数据
            l, r = queue.pop()
            # 先判断根节点
            if l and r and (l.val == r.val):
                # 继续入栈
                queue.append((l.left, r.right))
                queue.append((l.right, r.left))
            # 如果是子节点，跳过
            elif l is None and r is None:
                continue
            # 如果值不相等返回false
            else:
                return False
        return True


if __name__ == '__main__':
    r = '[3,9,20,null,null,15,7]'
    root = create_tree(r)
    print(Solution().isSymmetric(root))
