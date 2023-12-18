# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index_h = 0
        len_n = len(needle)
        while len_n <= len(haystack):
            if haystack[index_h:len_n] == needle:
                return index_h
            index_h += 1
            len_n += 1
        return -1
# leetcode submit region end(Prohibit modification and deletion)
