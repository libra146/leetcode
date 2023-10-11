from collections import defaultdict
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
        self.height = defaultdict(int)
        self.res = []

    def get_height(self, root):
        if not root:
            return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        self.height[root] = max(left, right) + 1
        return self.height[root]

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        self.get_height(root)
        self.res = [0] * (len(self.height) + 1)
        self.traverse(root, -1, 0)
        for index, value in enumerate(queries):
            queries[index] = self.res[value]
        return queries

    def traverse(self, root, depth, res_h):
        if not root:
            return
        self.res[root.val] = res_h
        depth += 1
        self.traverse(root.left, depth, max(self.res[root.val], depth + self.height[root.right]))
        self.traverse(root.right, depth, max(self.res[root.val], depth + self.height[root.left]))

# leetcode submit region end(Prohibit modification and deletion)
