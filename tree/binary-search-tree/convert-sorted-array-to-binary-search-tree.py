from typing import Optional, List

from utils import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums, lo, hi):
        if lo > hi:
            return
        middle = lo + (hi - lo) // 2
        root = TreeNode(nums[int(middle)])
        root.left = self.build(nums, lo, middle - 1)
        root.right = self.build(nums, middle + 1, hi)
        return root
