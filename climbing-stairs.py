# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.dp = {}

    def climbStairs(self, n: int) -> int:
        return self.ddp(n)

    def ddp(self, n):
        if self.dp.get(n, None) is not None:
            return self.dp.get(n)
        if n <= 2:
            return n
        res = 0
        for a in [1, 2]:
            res += self.ddp(n - a)
        self.dp[n] = res
        return res

# leetcode submit region end(Prohibit modification and deletion)
