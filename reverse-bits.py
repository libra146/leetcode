# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseBits(self, n: int) -> int:
        res = list(bin(n)[2:])
        if len(res) != 32:
            res = ['0'] * (32 - len(res)) + res
        res.reverse()
        return int(''.join(res), 2)
# leetcode submit region end(Prohibit modification and deletion)
