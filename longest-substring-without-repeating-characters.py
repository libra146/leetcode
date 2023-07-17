class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = []
        result = []
        for a in s:
            if a not in m:
                m.append(a)
            else:
                result.append(len(m))
                m = m[m.index(a) + 1:]
                m.append(a)
        result.append(len(m))
        return max(result)


# 双指针写法
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        window = {}
        res = 0
        while right < len(s):
            ss = s[right]
            right += 1
            window[ss] = window.get(ss, 0) + 1
            while window[ss] > 1:
                s2 = s[left]
                left += 1
                window[s2] -= 1
            res = max(res, right - left)
        return res


if __name__ == '__main__':
    # print(Solution().lengthOfLongestSubstring('abcabcbb'))
    print(Solution2().lengthOfLongestSubstring('abcabcbb'))
