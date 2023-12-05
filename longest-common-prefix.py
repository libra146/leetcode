from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_l = len(strs[0])
        res = ''
        for a in range(str_l):
            cur = ''
            for s in strs:
                if s == '':
                    return ''
                if len(s) - 1 >= a:
                    if cur == '':
                        res += s[a]
                        cur = s[a]
                    if cur != s[a]:
                        return res[:-1]
                else:
                    return res[:-1]
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    Solution().longestCommonPrefix(["flower", "flow", "flight"])
