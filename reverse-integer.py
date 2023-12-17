# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            res = int(str(x)[::-1])
            return res if res < 2 ** 31 else 0
        else:
            res = -int(str(-x)[::-1])
            return res if res > -2 ** 31 else 0
# leetcode submit region end(Prohibit modification and deletion)
