# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addDigits(self, num: int) -> int:
        if not num:
            return num
        return (num - 1) % 9 + 1
# leetcode submit region end(Prohibit modification and deletion)
