from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))
# leetcode submit region end(Prohibit modification and deletion)
