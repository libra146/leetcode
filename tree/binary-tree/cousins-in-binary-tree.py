from typing import Optional

from utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = [root]
        res = []
        while q:
            res.clear()
            for a in range(len(q)):
                node = q.pop(0)
                if node.left:
                    if node.left.val == x or node.left.val == y:
                        res.append((node.left.val, node.val))
                    q.append(node.left)
                if node.right:
                    if node.right.val == x or node.right.val == y:
                        res.append((node.right.val, node.val))
                    q.append(node.right)
            if len(res) == 2 and res[0][1] != res[1][1]:
                print(res)
                return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
