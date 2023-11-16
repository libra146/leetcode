from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for a in range(len(nums)):
            res ^= nums[a]
        return res

# leetcode submit region end(Prohibit modification and deletion)
