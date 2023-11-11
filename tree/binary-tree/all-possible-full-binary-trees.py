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
        self.cache = {}

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        return self.generate(n)

    def generate(self, n):
        if n in self.cache:
            return self.cache.get(n)
        if n == 1:
            return [TreeNode(0)]
        res = []
        for a in range(1, n, 2):
            left = self.generate(a)
            right = self.generate(n - 1 - a)
            for aa in left:
                for bb in right:
                    root = TreeNode(0)
                    root.left = aa
                    root.right = bb
                    res.append(root)
        self.cache[n] = res
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    Solution().allPossibleFBT(3)
