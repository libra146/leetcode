from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        for index, a in enumerate(nums):
            if index % 2 == a % 2:
                continue
            else:
                for i in range(index + 1, len(nums), 1):
                    if nums[i] % 2 == index % 2:
                        nums[index], nums[i] = nums[i], nums[index]
                        break
        return nums
# leetcode submit region end(Prohibit modification and deletion)
