from typing import List, Optional

from utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = {}

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        max_count = max(self.res.values())
        return [k for k, v in self.res.items() if v == max_count]

    def traverse(self, root):
        if not root:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        s = root.val + left + right
        if s in self.res:
            self.res[s] += 1
        else:
            self.res[s] = 1
        return s
# leetcode submit region end(Prohibit modification and deletion)
