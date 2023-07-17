"""
四种主要的遍历思想为：

前序遍历：根结点 ---> 左子树 ---> 右子树

中序遍历：左子树---> 根结点 ---> 右子树

后序遍历：左子树 ---> 右子树 ---> 根结点

层次遍历：只需按层次遍历即可
"""
from typing import List, Optional

from utils.TreeNode import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))
        return result


class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = [root]
        result = []
        while len(queue) > 0:
            q = queue.pop()
            if isinstance(q, TreeNode):
                queue.append(q.right)
                queue.append(q.val)
                queue.append(q.left)
            else:
                result.append(q)
        return result
