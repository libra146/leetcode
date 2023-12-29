# leetcode submit region begin(Prohibit modification and deletion)
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n
        mid = left + (right - left) // 2
        while mid < right:
            if guess(mid) == 1:
                left = mid + 1
            elif guess(mid) == -1:
                right = mid
            else:
                return mid
            mid = left + (right - left) // 2
        return mid
    # leetcode submit region end(Prohibit modification and deletion)
