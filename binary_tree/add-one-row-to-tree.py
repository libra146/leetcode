from typing import Optional

from utils import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val=val, left=root)
        d = 2
        queue = [root]
        while queue:
            q_len = len(queue)
            # 遍历当前层
            for _ in range(q_len):
                n = queue.pop(0)
                # 如果层数是对的，执行插入逻辑
                if d == depth:
                    # 实际插入节点
                    n.left = TreeNode(val=val, left=n.left)
                    n.right = TreeNode(val=val, right=n.right)
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            # 当前层遍历完成后进入下一层
            d += 1
        return root


class Solution2:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return
        if depth == 1:
            return TreeNode(val=val, left=root)
        if depth == 2:
            root.left = TreeNode(val=val, left=root.left)
            root.right = TreeNode(val=val, right=root.right)
        else:
            root.left = self.addOneRow(root.left, val, depth - 1)
            root.right = self.addOneRow(root.right, val, depth - 1)
        return root
