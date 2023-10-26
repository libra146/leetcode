# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        for a in str(num):
            if num % int(a) == 0:
                res += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
