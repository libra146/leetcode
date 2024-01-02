from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for a in nums:
            if a == 1:
                count += 1
            if a == 0:
                res = max(res, count)
                count = 0
        res = max(res, count)
        return res
# leetcode submit region end(Prohibit modification and deletion)
