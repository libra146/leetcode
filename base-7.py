# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convertToBase7(self, num: int) -> str:
        if abs(num) <= 6:
            return str(num)
        f = -1 if num < 0 else 1
        num = abs(num)
        res = []
        while num != 0:
            res.append(str(num % 7))
            num //= 7
        res.reverse()
        res = ''.join(res)
        return res if f == 1 else '-' + res

    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().convertToBase7(100)
