import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = collections.Counter(s)
        ans = 0
        for a in count.values():
            ans += a // 2 * 2
            if ans % 2 == 0 and a % 2 == 1:
                ans += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
