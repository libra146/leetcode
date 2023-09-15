from typing import List

from utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        print(nums)
        if not nums:
            return
        return self.create(nums, 0, len(nums))

    def create(self, nums, min_, max_):
        if min_ >= max_:
            return
        mid = (min_ + max_) // 2
        root = TreeNode(nums[mid])
        root.left = self.create(nums, min_, mid)
        root.right = self.create(nums, mid + 1, max_)
        return root
# leetcode submit region end(Prohibit modification and deletion)
