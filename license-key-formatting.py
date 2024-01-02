# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        if len(s) < k:
            return s
        if len(s) % k == 0:
            return '-'.join([s[i:i + k] for i in range(0, len(s), k)])
        else:
            return s[0:len(s) % k] + '-' + '-'.join([s[i:i + k] for i in range(len(s) % k, len(s), k)])
# leetcode submit region end(Prohibit modification and deletion)
