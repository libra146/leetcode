# leetcode submit region begin(Prohibit modification and deletion)
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        mid = left + (right - left) // 2
        while mid < right:
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
            mid = left + (right - left) // 2
        return left if isBadVersion(left) else right
# leetcode submit region end(Prohibit modification and deletion)
