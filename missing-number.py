from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        pre = nums[0]
        if pre != 0:
            return 0
        for a in nums:
            if a - pre > 1:
                return pre + 1
            pre = a
        return pre + 1
# leetcode submit region end(Prohibit modification and deletion)
