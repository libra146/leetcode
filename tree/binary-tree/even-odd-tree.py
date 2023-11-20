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
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        level = 0
        while queue:
            res = []
            for a in range(len(queue)):
                node = queue.pop(0)
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if self.is_sorted(res, level % 2 == 0):
                level += 1
                continue
            else:
                return False
        return True

    def is_sorted(self, res, asc):
        r = 0 if asc else float('inf')
        for a in res:
            if asc:
                if r < a and a % 2 != 0:
                    r = a
                else:
                    return False
            else:
                if r > a and a % 2 == 0:
                    r = a
                else:
                    return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
