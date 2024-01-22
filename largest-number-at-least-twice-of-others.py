from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_ = nums[0]
        max_index = 0
        se = nums[1]
        for index, a in enumerate(nums):
            if a > max_:
                se = max_
                max_index = index
                max_ = a
            elif a > se and a != max_:
                se = a
        return max_index if max_ >= 2 * se else -1
# leetcode submit region end(Prohibit modification and deletion)
