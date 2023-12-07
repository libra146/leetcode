# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        y = 0
        while temp > 0:
            t = temp % 10
            temp = temp // 10
            y = y * 10 + t
        return y == x
# leetcode submit region end(Prohibit modification and deletion)
