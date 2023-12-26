# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isHappy(self, n: int) -> bool:
        i = 0
        while i <= 810:
            n = sum(map(lambda x: int(x) ** 2, list(str(n))))
            if n == 1:
                return True
            i += 1
        return False
# leetcode submit region end(Prohibit modification and deletion)
