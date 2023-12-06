from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
# leetcode submit region end(Prohibit modification and deletion)
