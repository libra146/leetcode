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
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root]
        level = 0
        while queue:
            tmp = []
            level += 1
            for a in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node)
                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)
            if level % 2 == 0:
                for a in range(int(len(tmp) / 2)):
                    tmp[a].val, tmp[-(a + 1)].val = tmp[-(a + 1)].val, tmp[a].val
        return root
# leetcode submit region end(Prohibit modification and deletion)
