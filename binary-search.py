from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                return mid
        return -1


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    Solution().search([-1, 0, 3, 5, 9, 12], 2)
